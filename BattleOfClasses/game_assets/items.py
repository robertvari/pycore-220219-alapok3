class ItemBase:
    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price

    def report(self):
        print(f"Name: {self._name}")
        print(f"Weight: {self._weight}")
        print(f"Price: {self._price}")

    def use(self):
        print(f"Use {self._name}")


class Weapon(ItemBase):
    def use(self):
        print(f"Attack with a {self._name}")


class Food(ItemBase):
    def use(self):
        print(f"Eat a {self._name}")


class Cloth(ItemBase):
    def use(self):
        print(f"Get a nice {self._name}")


class Inventory:
    def __init__(self, name):
        self._name = name
        self._items = []

    def add_item(self, item):
        print(f"{item} added to {self._name}")
        self._items.append(item)

    def show(self):
        print(f"{self._items}")
        print(f"Weight: {0}")
        print(f"Value: {0}")

if __name__ == '__main__':
    sword = Weapon("Common Sword", 10, 24)
    bread = Food("Bread", 1, 3)
    hat = Cloth("Blue Hat", 3, 30)

    my_backpack = Inventory()
    my_backpack.add_item(sword)
    my_backpack.add_item(bread)
    my_backpack.add_item(hat)