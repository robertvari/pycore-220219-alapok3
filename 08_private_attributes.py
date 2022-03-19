class Dice:
    def __init__(self, color, sides):
        # protected instance attribute
        self._color = color

        # protected attribute
        self._sides = sides

        # private attribute
        self.__current_side = 1


my_dice = Dice("white", 6)
print(my_dice.__current_side)