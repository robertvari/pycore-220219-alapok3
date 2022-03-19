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

    def draw(self):
        new_card = self._cards[0]
        self._cards.remove(new_card)
        return new_card

    def __repr__(self):
        return f"{self._cards}"


class PlayerBase:
    def __init__(self):
        self._name = None
        self._hand = []
        self._credits = random.randint(10, 100)
        self._in_game = True

    def create(self):
        first_names = ["Brittney", "Curtis", "Lucas", "Chip", "Simon"]
        last_names = ["Moriah", "Tristin", "Troy", "Gale", "Lynn"]

    def __str__(self):
        return f"Name: {self._name}\nHand:{self._hand}\nCredits: {self._credits}"


class Player(PlayerBase):
    pass


class AIPlayer(PlayerBase):
    pass


player = Player()
ai_player = AIPlayer()

print(player)
print(ai_player)