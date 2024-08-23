from inventory import display_inventory, update_inventory, inventory
from customer_interaction import ask_for_item, ask_for_quantity, ask_to_add_more
from billing import calculate_total, display_bill
from payment import process_payment

def main():
    cart = {}
    print("Welcome to the Vending Machine!\n")

    while True:
        display_inventory()

        # Loop until a valid item is provided
        while True:
            item = ask_for_item().title()  # Normalize to title case

            if item not in inventory:
                print("Item not found. Please choose a valid item.\n")
            else:
                break

        # Loop until a valid quantity is provided
        while True:
            quantity = ask_for_quantity()

            if quantity > inventory[item]['quantity']:
                print(f"Sorry, only {inventory[item]['quantity']} {item}(s) are available.")
            else:
                break

        # Add item to the cart
        if item in cart:
            cart[item]['quantity'] += quantity
        else:
            cart[item] = {'price': inventory[item]['price'], 'quantity': quantity}

        # Update inventory
        update_inventory(item, quantity)

        # Ask if the customer wants to add more items
        if not ask_to_add_more():
            break

    # Calculate total, display bill, and process payment
    total = calculate_total(cart)
    display_bill(cart, total)
    process_payment(total)

if __name__ == "__main__":
    main()
