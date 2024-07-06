class MenuItem:
    """Models the Menu with drinks."""
    def __init__(self, name, cost, water, milk, coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {"water": water, "milk": milk, "coffee": coffee}


class Menu:
    """Returns all the names of the available menu items"""
    def __init__(self):
        self.menu = [
            MenuItem("latte", 2.5, 200, 150, 24),
            MenuItem("espresso", 1.5, 50, 0, 18),
            MenuItem("cappuccino", 3, 250, 50, 24),
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
