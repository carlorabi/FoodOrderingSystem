class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def calculate_total_spent(self):
        total_spent = 0
        for order in self.orders:
            total_spent += order.calculate_total_cost()
        return total_spent
