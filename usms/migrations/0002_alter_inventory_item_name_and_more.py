# Generated by Django 4.1 on 2023-07-29 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usms", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inventory",
            name="Item_Name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="Vendor_Name",
            field=models.CharField(default="", max_length=100),
        ),
    ]
