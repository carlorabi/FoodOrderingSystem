# order.py
from menu_item import MenuItem

class Order:
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

    def calculate_total_cost(self):
        total_cost = 0
        for item in self.items:
            total_cost += item.price
        return total_cost
