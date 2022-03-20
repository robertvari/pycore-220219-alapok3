from game_assets.assets import Deck, Player, AIPlayer


class Blackjack:
    def __init__(self):
        # Blackjack member attributes
        self._player_list = []
        self._bet = 0
        self._deck = Deck()

        self._intro()

        # create players
        self._player_list.append(Player())

        # create AI Players
        for _ in range(3):
            self._player_list.append(AIPlayer())

        self._start_game()

    @staticmethod
    def _intro():
        print("-" * 50, "BLACKJACK", "-" * 50)

    def _start_game(self):
        self._deck.create()
        self._bet = 0

        for player in self._player_list:
            self._bet += player.give_bet(10)
            player.set_start_hand(self._deck)
            player.draw_card(self._deck)

        print("-"*50)

        for player in self._player_list:
            player.show_hand()

Blackjack()