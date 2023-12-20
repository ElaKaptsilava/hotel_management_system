# Generated by Django 5.0 on 2023-12-19 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reports", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hotelreport",
            name="hotel",
        ),
        migrations.AddField(
            model_name="hotelreport",
            name="hotel_name",
            field=models.CharField(default="hotel", max_length=256),
        ),
    ]
