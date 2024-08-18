
def ask_for_item():
    item = input("\nPlease enter the item you want to purchase:")
    return item

def ask_for_quantity():
    quantity = int(input("\n Please enter the quantity you want:"))
    return quantity

def ask_to_add_more():
    response = input("\nDo you want to add more items? (yes/no):")
    return response.lower() == 'yes'
