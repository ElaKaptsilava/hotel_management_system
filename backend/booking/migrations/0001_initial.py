# Generated by Django 5.0.4 on 2024-04-08 14:22

import django.db.models.deletion
import django.db.models.expressions
import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("hotel_management", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "check_in",
                    models.DateField(
                        default=django.utils.timezone.now,
                        help_text="Specify the check-in date.",
                    ),
                ),
                (
                    "check_out",
                    models.DateField(
                        default=django.utils.timezone.now,
                        help_text="Specify the check-out date.",
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None
                    ),
                ),
                (
                    "duration",
                    models.GeneratedField(
                        db_persist=True,
                        expression=django.db.models.expressions.CombinedExpression(
                            models.F("check_out"), "-", models.F("check_in")
                        ),
                        null=True,
                        output_field=models.DurationField(),
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        help_text="Specify the room.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hotel_management.room",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="Select the user who is making the booking.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
