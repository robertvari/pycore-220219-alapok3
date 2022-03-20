from game_assets.items import Inventory

races = {
    "human": {"strength": 50, "max_HP": 100, "max_weight": 50},
    "ork": {"strength": 130, "max_HP": 200, "max_weight": 100},
    "elf": {"strength": 60, "max_HP": 100, "max_weight": 60},
    "dwarf": {"strength": 130, "max_HP": 230, "max_weight": 150},
}


class CharacterBase:
    def __init__(self):
        self._name = None
        self._race = None
        self._golds = 0
        self._max_weight = 0
        self._inventory = Inventory("Backpack")

        # combat stats
        self._strength = 0
        self._max_HP = 0
        self._current_HP = 0

        self._right_hand = None
        self._left_hand = None

    def _create(self):
        pass


class Player(CharacterBase):
    pass


class Enemy(CharacterBase):
    pass


if __name__ == '__main__':
    enemy = Enemy()
    player = Player()