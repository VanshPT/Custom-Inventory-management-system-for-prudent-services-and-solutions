from django.db import models

# Create your models here.
class Inventory(models.Model):
    Sr_No = models.AutoField(primary_key=True)
    CHOICES = (
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    )
    Item_Name = models.CharField(max_length=100, choices=CHOICES)
    Purchase_Quantity = models.CharField(max_length=100, default="")
    Cost_Per_Item = models.IntegerField(default="")
    Other_Cost = models.CharField(max_length=100, default="")
    CHOICES1 = (
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('option4', 'Option 4'),
        ('option5', 'Option 5'),
    )
    Vendor_Name = models.CharField(max_length=100, choices=CHOICES1, default="")
    Date_of_Purchase = models.DateField()
    Surat_Stock = models.IntegerField()
    Daman_Stock = models.IntegerField()
    Ankleshvar_Stock = models.IntegerField()
    Reorder_Quantity = models.IntegerField(default="")

    def __str__(self):
        return self.Item_Name
    
class Item(models.Model):
    Item_Code = models.CharField(max_length=30, unique=True)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.Item_Code