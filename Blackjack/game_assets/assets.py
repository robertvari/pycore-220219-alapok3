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

        self._create()

    def _create(self):
        first_names = ["Brittney", "Curtis", "Lucas", "Chip", "Simon"]
        last_names = ["Moriah", "Tristin", "Troy", "Gale", "Lynn"]
        self._name = f"{random.choice(first_names)} {random.choice(last_names)}"

    def set_start_hand(self, deck):
        self._hand.clear()

        for _ in range(2):
            self._hand.append(deck.draw())

    def draw_card(self, deck):
        while self._in_game:
            # check hand value
            hand_value = self._count_hand()

            if hand_value <= 16:
                print(f"{self._name} draws a new card")
                self._hand.append(deck.draw())
            else:
                print(f"{self._name} passes")
                self._in_game = False

    def _count_hand(self):
        return sum([card.value for card in self._hand])

    def show_hand(self):
        print(f"{self._name} hand: {self._hand} Hand value: {self._count_hand()}")

    def __str__(self):
        return f"Name: {self._name}\nHand:{self._hand}\nCredits: {self._credits}"


class Player(PlayerBase):
    # method override
    def _create(self):
        self._name = input("What is your name?")


class AIPlayer(PlayerBase):
    pass


if __name__ == '__main__':
    deck = Deck()

    player = Player()
    player.set_start_hand(deck)
    player.draw_card(deck)

    ai_player = AIPlayer()
    ai_player.set_start_hand(deck)
    ai_player.draw_card(deck)

    player.show_hand()
    ai_player.show_hand()
