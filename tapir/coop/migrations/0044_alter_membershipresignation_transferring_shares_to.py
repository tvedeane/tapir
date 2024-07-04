# Generated by Django 3.2.25 on 2024-07-04 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coop", "0043_auto_20240704_1414"),
    ]

    operations = [
        migrations.AlterField(
            model_name="membershipresignation",
            name="transferring_shares_to",
            field=models.OneToOneField(
                help_text="Leave this empty if the resignation type is not a transfer to another member",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="owner_to_transfer",
                to="coop.shareowner",
                verbose_name="OwnerToTransfer",
            ),
        ),
    ]
