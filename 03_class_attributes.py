class Dice:
    # class attributes
    color = "white"
    sides = 6


class Student:
    # class attributes
    name = None
    age = None
    address = None
    grade = None
    phone = None


robert = Student()
robert.name = "Robert Vari"


tom = Student()
tom.name = "Kiss Tamás"

print(robert.name)
print(tom.name)