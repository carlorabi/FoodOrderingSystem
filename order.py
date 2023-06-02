from order_item import OrderItem

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
            order_str += f"{index+1}. {order_item.menu_item.name}: ₱{order_item.menu_item.price:.2f} x {order_item.quantity}\n"
        return order_str.strip()