def calculate_total(cart):
    total = sum(details['price'] * details['quantity'] for item, details in cart.items())
    return total

def display_bill(cart, total):
    print("\n" + "="*30)
    print(" " * 8 + "VENDING MACHINE")
    print("="*30)
    print("{:<10} {:>5} {:>7} {:>8}".format("Item", "Qty", "Price", "Total"))
    print("-" * 30)

    for item, details in cart.items():
        item_total = details['price'] * details['quantity']
        print("{:<10} {:>5} ${:>6.2f} ${:>7.2f}".format(item, details['quantity'], details['price'], item_total))

    print("-" * 30)
    print("{:<10} {:>5} {:>7} ${:>7.2f}".format("Total", "", "", total))
    print("="*30 + "\n")
