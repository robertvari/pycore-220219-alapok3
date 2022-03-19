class Card:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    def __repr__(self):
        return f"{self._name} {self._value}"


card = Card("Spade King", 10)
print(card.name)
print(card.value)
print(card)

