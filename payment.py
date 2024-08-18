def process_payment(total):
    remaining_amount = total
    while remaining_amount > 0:
        amount_paid = float(input(f"Please enter the remaining amount of ${remaining_amount:.2f}: "))
        if amount_paid >= remaining_amount:
            change = amount_paid - remaining_amount
            print(f"Payment successful! Thank you! Your change is ${change:.2f}.")
            break
        else:
            remaining_amount -= amount_paid
            print(f"Insufficient amount. You need to pay ${remaining_amount:.2f} more.")
