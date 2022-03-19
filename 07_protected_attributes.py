class Dice:
    def __init__(self, color, sides):
        # protected instance attribute
        self._color = color

        # protected attribute
        self._sides = sides

        # public attribute
        self.current_side = 1


my_dice = Dice("white", 6)
print(my_dice._color)
print(my_dice._sides)

print(my_dice.current_side)