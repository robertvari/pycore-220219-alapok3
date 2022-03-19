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


class Deck:
    def __init__(self):
        self._cards = []

        self.create()

    def create(self):
        self._cards.clear()

    def __repr__(self):
        return f"{self._cards}"


deck = Deck()
print(deck)