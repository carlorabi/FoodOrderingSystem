import os
from datetime import datetime

def print_receipt(customer, bill_amount, remaining_balance):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print("\n----------- Receipt -----------")
    print(f"Customer: {customer.name}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
    print("--------------------------------")
    print("Order Details:")
    total_spent = 0
    for order in customer.orders:
        print("Order:")
        for index, order_item in enumerate(order.items, start=1):
            subtotal = order_item.menu_item.price * order_item.quantity
            total_spent += subtotal
            print(f"{index}. {order_item.menu_item.name:<20} ₱{order_item.menu_item.price:>6.2f} x {order_item.quantity:>2} = ₱{subtotal:>7.2f}")
    print("--------------------------------")
    print(f"Total spent: ₱{total_spent:>7.2f}")
    print(f"Bill amount: ₱{bill_amount:>7.2f}")
    print(f"Change: ₱{remaining_balance:>9.2f}")
    print("--------------------------------")
    print("Thank you for your purchase!")
    print("-------------------------------")

