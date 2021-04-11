import enum
from decimal import Decimal

from django.conf import settings
from django.db import models

from tapir.accounts.models import TapirUser
from tapir.odoo.models import OdooAPI, OdooModel, OdooPartner

_ODOO_INVOICE_MODEL_NAME = "account.invoice"


class InvoiceManager(models.Manager):
    def create_with_user(self, user: TapirUser):
        odoo_id = self.model._odoo_create({"partner_id": user.odoo_partner.odoo_id})
        return self.create(odoo_id=odoo_id, user=user)

    def create_with_odoo_partner(self, odoo_partner: OdooPartner):
        odoo_id = self.model._odoo_create({"partner_id": odoo_partner.odoo_id})
        return self.create(odoo_id=odoo_id)


class Invoice(OdooModel):
    objects = InvoiceManager()
    odoo_model_name = "account.invoice"

    odoo_id = models.IntegerField(blank=False, null=False, unique=True)

    # May be NULL if this Invoice is attached to a DraftUser for the moment
    user = models.ForeignKey(
        TapirUser,
        related_name="invoices",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )

    class State(enum.IntEnum):
        DRAFT = 1
        OPEN = 2
        PAID = 3

    def get_state(self):
        raw = self._odoo_get_field("state")
        if raw == "draft":
            return Invoice.State.DRAFT
        elif raw == "open":
            return Invoice.State.OPEN
        elif raw == "paid":
            return Invoice.State.PAID

    def add_invoice_line(self, name, amount: Decimal, tax_id):
        OdooAPI.get_connection().create(
            "account.invoice.line",
            {
                "invoice_id": self.odoo_id,
                "name": name,
                "price_unit": str(amount),
                "quantity": 1,
                "account_id": 1151,
                # Uses the Many2Many command format documented in the odoo API docs.
                # The command (6, 0, x) replaces all existing entries
                "invoice_line_tax_ids": [(6, 0, [tax_id])],
            },
        )

    def get_total_amount(self) -> Decimal:
        return Decimal(self._odoo_get_field("amount_total_signed"))

    def register_payment(self, amount: Decimal, journal_id):
        assert amount > 0

        self_fields = self._odoo_get(["partner_id", "reference"])
        partner_id = self_fields["partner_id"][0]
        reference = self_fields["reference"]
        payment_id = OdooAPI.get_connection().create(
            "account.payment",
            {
                "journal_id": journal_id,
                "invoice_ids": [(6, 0, [self.odoo_id])],
                "amount": str(amount),
                "payment_type": "inbound",
                # NOTE(Leon Handreke): I have no idea what this does, all payments seem to have the same if
                # registered manually
                "payment_method_id": 1,  # Manual (inbound)
                "partner_id": partner_id,
                "communication": "{} via Tapir".format(reference),
                "partner_type": "customer",
            },
        )

        OdooAPI.get_connection().execute(
            "account.payment", "action_validate_invoice_payment", [payment_id], {}
        )