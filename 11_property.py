class Dice:
    def __init__(self, sides, color):
        self.__sides = sides
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        assert isinstance(new_color, str), "color must be of type str"
        self.__color = new_color


my_dice = Dice(6, "white")
print(my_dice.color)
my_dice.color = 10

print(my_dice.color)