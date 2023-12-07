# Generated by Django 4.2.7 on 2023-12-07 13:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("hotel_management", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discount",
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
                ("value", models.IntegerField()),
                ("is_percentage", models.BooleanField(default=True)),
                (
                    "room",
                    models.ManyToManyField(default=list, to="hotel_management.room"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
