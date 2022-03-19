class Student:
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def __str__(self):
        return f"Name: {self._name} Email: {self._email}"


class Dice:
    def __init__(self, sides, color):
        self._sides = sides
        self._color = color

    def __str__(self):
        return f"Sides: {self._sides} Color: {self._color}"

    def __repr__(self):
        return f"{self._color}: {self._sides}"


tamas = Student("Kiss Tamás", "tamas@gmail.com")
print(tamas)

robert = Student("Robert Vari", "robert@gmail")
print(robert)

my_dice1 = Dice("Red", 6)
my_dice2 = Dice("Blue", 10)
my_dice3 = Dice("Green", 20)

my_fave_dices = [my_dice1, my_dice2, my_dice3]
print(my_fave_dices)