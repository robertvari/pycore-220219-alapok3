from game_assets.assets import Deck


class Blackjack:
    def __init__(self):
        self._intro()

        self._deck = Deck()

    @staticmethod
    def _intro():
        print("-" * 50, "BLACKJACK", "-" * 50)


Blackjack()