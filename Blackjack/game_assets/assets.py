import random


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

        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]

        names = ["Heart", "Club", "Diamond", "Spade"]

        for suit in names:
            for card in cards:
                new_card = Card(f"{suit} {card[0]}", card[1])
                self._cards.append(new_card)

        random.shuffle(self._cards)

    def __repr__(self):
        return f"{self._cards}"


deck = Deck()
print(deck)