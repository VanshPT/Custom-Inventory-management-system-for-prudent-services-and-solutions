# Generated by Django 4.1 on 2023-07-29 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usms", "0002_alter_inventory_item_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inventory",
            name="Item_Name",
            field=models.CharField(
                choices=[
                    ("option1", "Option 1"),
                    ("option2", "Option 2"),
                    ("option3", "Option 3"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="Vendor_Name",
            field=models.CharField(
                choices=[
                    ("option1", "Option 1"),
                    ("option2", "Option 2"),
                    ("option3", "Option 3"),
                    ("option4", "Option 4"),
                    ("option5", "Option 5"),
                ],
                default="",
                max_length=100,
            ),
        ),
    ]
