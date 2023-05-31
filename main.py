from menu import Menu
from customer import Customer
from order import Order
from order_item import OrderItem
from banner import print_banner
import os

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                return True
        return False

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def display_menu(self):
        print("Menu:")
        if not self.items:
            print("No items in the menu.")
        else:
            for item in self.items:
                print(item)


class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    def get_subtotal(self):
        return self.menu_item.price * self.quantity

    def __str__(self):
        return f"{self.menu_item.name} (Quantity: {self.quantity})"


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item, quantity):
        order_item = OrderItem(menu_item, quantity)
        self.items.append(order_item)

    def calculate_total_cost(self):
        total_cost = 0
        for order_item in self.items:
            total_cost += order_item.menu_item.price * order_item.quantity
        return total_cost

    def __str__(self):
        order_str = ""
        for index, order_item in enumerate(self.items):
            order_str += f"{index+1}. {order_item.menu_item.name}: ${order_item.menu_item.price:.2f} x {order_item.quantity}\n"
        return order_str.strip()





def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def place_order(menu, customer):
    order = Order()

    print(f"Welcome, {customer.name}!")
    display_menu(menu)

    while True:
        choice = input("Enter the name of the item you want to order (or 'q' to quit): ")

        if choice == 'q':
            break

        item = menu.find_item(choice)
        if item:
            quantity = int(input("Enter the quantity: "))
            order.add_item(item, quantity)
            print(f"{item.name}: ${item.price:.2f} x {quantity} added to your order.")
        else:
            print("Invalid choice. Please try again.")
            continue

        while True:
            add_another = input("Do you want to add another item? (y/n): ")
            if add_another.lower() == 'n':
                break
            elif add_another.lower() != 'y':
                print("Invalid input. Please enter 'y' or 'n'.")
            else:
                break

    print("Your order:")
    for index, order_item in enumerate(order.items):
        print(f"{index+1}. {order_item.menu_item.name}: ${order_item.menu_item.price:.2f} | Quantity: {order_item.quantity}")

    total_cost = order.calculate_total_cost()
    print(f"Total cost: ${total_cost:.2f}")

    while True:
        action = input("\nDo you want to make any changes to your order? (1 - Change item, 2 - Change quantity, 3 - Delete item, 4 - Continue): ")

        if action == '1':
            cls()
            print("Current order:")
            for index, item in enumerate(order.items, start=1):
                print(f"{index}. {item.menu_item.name}: ${item.menu_item.price:.2f} x Quantity {item.quantity}")
            item_name = input("Enter the name of the item you want to change: ")
            found_item = False
            for order_item in order.items:
                if order_item.menu_item.name.lower() == item_name.lower():
                    new_item_name = input("Enter the new item name: ")
                    new_item_quantity = int(input("Enter the new quantity: "))
                    new_item = menu.find_item(new_item_name)
                    if new_item:
                        order_item.menu_item = new_item
                        order_item.quantity = new_item_quantity
                        print("Item updated successfully.")
                    else:
                        print("Invalid item name. Item not updated.")
                    found_item = True
                    break
            if not found_item:
                print("Item not found in the order.")

        elif action == '2':
            cls()
            print("Current order:")
            for index, item in enumerate(order.items, start=1):
                print(f"{index}. {item.menu_item.name}: ${item.menu_item.price:.2f} x Quantity {item.quantity}")
            item_name = input("Enter the name of the item you want to change quantity: ")
            found_item = False
            for order_item in order.items:
                if order_item.menu_item.name.lower() == item_name.lower():
                    new_quantity = int(input("\nEnter the new quantity: "))
                    if new_quantity > 0:
                        order_item.quantity = new_quantity
                        print("Quantity updated successfully.")
                        print("\nUpdated order:")
                        for index, order_item in enumerate(order.items, start=1):
                            print(f"{index}. {order_item.menu_item.name}: ${order_item.menu_item.price:.2f} x Quantity {order_item.quantity}")

                    else:
                        print("Invalid quantity. Quantity not updated.")
                    found_item = True
                    break
            if not found_item:
                print("Item not found in the order.")
                # Print the updated order

        elif action == '3':
            cls()
            print("Current order:")
            for index, item in enumerate(order.items, start=1):
                print(f"{index}. {item.menu_item.name}: ${item.menu_item.price:.2f} x Quantity {item.quantity}")
            item_name = input("Enter the name of the item you want to delete: ")
            found_item = False
            for order_item in order.items:
                if order_item.menu_item.name.lower() == item_name.lower():
                    order.items.remove(order_item)
                    print(f"{order_item} deleted from the order.")
                    found_item = True
                    break
            if not found_item:
                print("Item not found in the order.")

        elif action == '4':
            break
        else:
            print("Invalid choice. Please try again.")

    customer.add_order(order)


def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/Mac


def display_menu(menu):
    print("Menu:")
    print("-----------------------------------------")
    print("| {:<17s} | {:>17s} |".format("Food", "Price"))
    print("-----------------------------------------")
    for item in menu.items:
        print("| {:<17s} | {:>17.2f} |".format(item.name, item.price))
    print("-----------------------------------------")



# Main program
menu = Menu()

item1 = MenuItem("Burger", 5.99)
item2 = MenuItem("Pizza", 8.99)
item3 = MenuItem("Fries", 2.99)
item4 = MenuItem("Salad", 4.99)
item5 = MenuItem("Ice Cream", 3.99)

menu.add_item(item1)
menu.add_item(item2)
menu.add_item(item3)
menu.add_item(item4)
menu.add_item(item5)

customers = []


def print_menu_button(label):
    print(f"  \u25A0 {label} \u25A0  ")


while True:
    clear_screen()
    print_banner()
    print()
    print_menu_button("1. Show Menu")
    print_menu_button("2. Add Item to Menu")
    print_menu_button("3. Remove Item from Menu")
    print_menu_button("4. Place Order")
    print_menu_button("5. Total Orders for Customer")
    print_menu_button("6. Exit")

    choice = input("\nEnter the number of your choice: ")

    # Rest of your code...


    if choice == '1':
        clear_screen()
        display_menu(menu)
        input("Press Enter to continue...")

    elif choice == '2':
        while True:
            clear_screen()
            item_name = input("Enter the name of the item: ")
            while True:
                try:
                    item_price = float(input("Enter the price of the item: $"))
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            new_item = MenuItem(item_name, item_price)
            menu.add_item(new_item)
            print(f"{item_name} added to the menu.")
            while True:
                add_another = input("Do you want to add another item? (y/n): ")
                if add_another.lower() == 'n':
                    break
                elif add_another.lower() == 'y':
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
            if add_another.lower() == 'n':
                break
            elif add_another.lower() != 'y':
                continue


    elif choice == '3':
        clear_screen()
        display_menu(menu)
        item_name = input("Enter the name of the item you want to remove: ")
        if menu.remove_item(item_name):
            print(f"{item_name} removed from the menu.")
        else:
            print("Item not found in the menu.")
        input("Press Enter to continue...")

    elif choice == '4':
        clear_screen()
        customer_name = input("Enter your name: ")
        customer = None
        for c in customers:
            if c.name.lower() == customer_name.lower():
                customer = c
                break
        if not customer:
            customer = Customer(customer_name)
            customers.append(customer)
        place_order(menu, customer)
        input("Press Enter to continue...")

    elif choice == '5':
        if not customers:
            print("\nNo customer(s) yet.")
            input("Press Enter to continue...")
            continue

        print("Customers:")
        for customer in customers:
            print(customer.name)

        customer_name = input("\nEnter the name of the customer: ")
        for customer in customers:
            if customer.name.lower() == customer_name.lower():
                total_spent = customer.calculate_total_spent()
                print(f"Total spent by {customer.name}: ${total_spent:.2f}")
                print("Customer's orders:")
                for order in customer.orders:
                    print("Order:")
                    for index, order_item in enumerate(order.items, start=1):
                        print(f"{index}. {order_item.menu_item.name}: ${order_item.menu_item.price:.2f} x Quantity {order_item.quantity}")
                while True:
                    bill_amount = input("Enter the bill amount: $")
                    try:
                        bill_amount = float(bill_amount)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")
                remaining_balance = bill_amount - total_spent
                print(f"Change for {customer.name}: ${remaining_balance:.2f}")
                break
        else:
            print("Customer not found.")
            
        input("Press Enter to continue...")



    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")
