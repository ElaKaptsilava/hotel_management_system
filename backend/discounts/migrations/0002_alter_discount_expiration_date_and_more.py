# Generated by Django 5.0 on 2024-04-07 12:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("discounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount",
            name="expiration_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="discount",
            name="generated",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
