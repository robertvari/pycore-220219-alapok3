class Student:
    # class methods
    # the constructor
    def __init__(self, name, age, address, email):
        self.name = name
        self.age = age
        self.address = address
        self.email = email


robert = Student(
    "Robert Vari",
    32,
    "Budapest",
    "robert@gmail.com"
)

print(robert.name)
print(robert.age)
print(robert.address)
print(robert.email)


tamas = Student(
    "Kiss Tamás",
    23,
    "Pécs",
    "tamas@gmail.com"
)

print(tamas.name)
print(tamas.age)
print(tamas.address)
print(tamas.email)