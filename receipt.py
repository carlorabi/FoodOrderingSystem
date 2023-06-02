from datetime import datetime

def print_receipt(customer, bill_amount, remaining_balance):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\n---------- Receipt ----------")
    print(f"Date: {current_date}")
    print(f"Customer: {customer.name}")
    for order in customer.orders:
        print("\nOrder(s):")
        for index, order_item in enumerate(order.items, start=1):
            print(f"{index}. {order_item.menu_item.name}: ₱{order_item.menu_item.price:.2f} | Quantity: {order_item.quantity}")
    print(f"Total: ₱{customer.calculate_total_spent():.2f}")
    print(f"Bill amount: ₱{bill_amount:.2f}")
    print(f"Change: ₱{remaining_balance:.2f}")
    print("-------------------------------")