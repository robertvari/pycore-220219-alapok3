class ItemBase:
    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price

    def report(self):
        print(f"Name: {self._name}")
        print(f"Weight: {self._weight}")
        print(f"Price: {self._price}")


class Weapon(ItemBase):
    pass


class Food(ItemBase):
    pass


class Cloth(ItemBase):
    pass


if __name__ == '__main__':
    sword = Weapon("Common Sword", 10, 24)
    bread = Food("Bread", 1, 3)
    hat = Cloth("Blue Hat", 3, 30)