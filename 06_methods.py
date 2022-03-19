import random


class Dice:
    def __init__(self, color, sides):
        self.color = color,
        self.sides = sides
        self.current_side = 1

    def roll(self):
        self.current_side = random.randint(1, self.sides)
        print(f"Dice {self.sides}: {self.current_side}")


my_dice1 = Dice("red", 10)
my_dice2 = Dice("blue", 6)

my_dice1.roll()
my_dice2.roll()