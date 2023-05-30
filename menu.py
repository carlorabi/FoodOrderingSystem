# menu.py
from menu_item import MenuItem

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
