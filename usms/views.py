from django.shortcuts import render
from .models import Inventory, Item

def index(request):
    items = Inventory.objects.values(
        'Sr_No', 'Item_Name', 'Purchase_Quantity', 'Cost_Per_Item', 'Other_Cost',
        'Vendor_Name', 'Date_of_Purchase', 'Surat_Stock', 'Daman_Stock',
        'Ankleshvar_Stock', 'Reorder_Quantity'
    )
    icode = Item.objects.values(
        'inventory__Item_Name', 'Item_Code'
    )
    
    # Calculate total stock and add it to each item dictionary
    for item in items:
        item['Total_Stock'] = item['Surat_Stock'] + item['Daman_Stock'] + item['Ankleshvar_Stock']
        item['Total_Inventory_Value']=item['Total_Stock']*item['Cost_Per_Item']
        item['Reorder_Value']=item['Reorder_Quantity']*item['Cost_Per_Item']
    
    params = {'items': items, 'icode': icode}
    return render(request, "usms/index.html", params)
