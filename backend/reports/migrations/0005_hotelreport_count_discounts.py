# Generated by Django 5.0 on 2023-12-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reports", "0004_alter_roomreport_amount_of_booking_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="hotelreport",
            name="count_discounts",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
