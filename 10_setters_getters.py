class Dice:
    def __init__(self, sides, color):
        self._sides = sides
        self._color = color

    def get_sides(self):
        return self._sides

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        assert isinstance(new_color, str), "color must be of type str"
        self._color = new_color


my_dice = Dice(6, "white")
print(my_dice.get_color())

my_dice.set_color(10)
print(my_dice.get_color())
