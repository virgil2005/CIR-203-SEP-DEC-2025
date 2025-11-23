inventory ={
    "Laptop":15,
    "Phone" :8,
    "Headphones" : 20,
    "Charger" : 5,
    "Tablet" : 12,
}
print("Inventory:",inventory)
inventory["Smartwatch"]= 10
inventory["Phone"] = 14
print("updated inventory:",inventory)
def low_stock(inv):
    return{k:v for k,v in inv.items() if v < 10}
    print("Low stock items:",low_stock(inventory))
del inventory["Charger"]
print("After removing Charger:",inventory)
for product,qty in inventory.items():
    print(f"{product}:{qty}" )