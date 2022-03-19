class Dice:
    # class attribute
    dice_count = 0

    def __init__(self):
        # instance attribute
        self.color = "red"
        self.sides = 10

        Dice.dice_count += 1


my_dice1 = Dice()

my_dice2 = Dice()
my_dice2.color = "blue"

my_dice3 = Dice()
my_dice3.color = "green"

print(Dice.dice_count)