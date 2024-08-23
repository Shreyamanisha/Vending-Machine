inventory = {
    'Coke': {'price': 1.50, 'quantity': 5},
    'Pepsi': {'price': 1.25, 'quantity': 5},
    'Water': {'price': 1.00, 'quantity': 5},
    'Chips': {'price': 1.75, 'quantity': 5}
}

def display_inventory():
    print("Available items:")
    for item, details in inventory.items():
        print(f"{item}: ${details['price']} (Quantity: {details['quantity']})")
    

def update_inventory(item, quantity):
    if item in inventory:
        inventory[item]['quantity'] -= quantity
