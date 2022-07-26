# Generated by Django 3.2.13 on 2022-06-26 12:43

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shifts", "0036_auto_20220604_1531"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shiftslot",
            name="warnings",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        (
                            "in_the_morning_everyone_helps_storage",
                            "I understand that all working groups help the Warenannahme & Lager working group until the shop opens.",
                        ),
                        (
                            "in_the_evening_everyone_helps_clean",
                            "I understand that all working groups help the Reinigung & Aufräumen working group after the shop closes.",
                        ),
                        (
                            "bread_picked_needs_a_vehicle",
                            "I understand that I need my own vehicle in order to pick up the bread. A cargo bike can be borrowed, more infos in Slack in the #cargobike channel",
                        ),
                        (
                            "must_be_able_to_carry_heavy_weights",
                            "I understand that I may need to carry heavy weights for this shift.",
                        ),
                        (
                            "must_not_be_scared_of_heights",
                            "I understand that I may need to work high, for example up a ladder. I do not suffer from fear of heigts.",
                        ),
                    ],
                    max_length=128,
                ),
                blank=True,
                default=list,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="shiftslottemplate",
            name="warnings",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        (
                            "in_the_morning_everyone_helps_storage",
                            "I understand that all working groups help the Warenannahme & Lager working group until the shop opens.",
                        ),
                        (
                            "in_the_evening_everyone_helps_clean",
                            "I understand that all working groups help the Reinigung & Aufräumen working group after the shop closes.",
                        ),
                        (
                            "bread_picked_needs_a_vehicle",
                            "I understand that I need my own vehicle in order to pick up the bread. A cargo bike can be borrowed, more infos in Slack in the #cargobike channel",
                        ),
                        (
                            "must_be_able_to_carry_heavy_weights",
                            "I understand that I may need to carry heavy weights for this shift.",
                        ),
                        (
                            "must_not_be_scared_of_heights",
                            "I understand that I may need to work high, for example up a ladder. I do not suffer from fear of heigts.",
                        ),
                    ],
                    max_length=128,
                ),
                blank=True,
                default=list,
                size=None,
            ),
        ),
    ]