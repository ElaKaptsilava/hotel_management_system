# Generated by Django 5.0 on 2023-12-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("discounts", "0002_rename_room_discount_rooms"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="discount",
            name="is_percentage",
        ),
        migrations.AddField(
            model_name="discount",
            name="percentage_value",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="discount",
            name="value",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
