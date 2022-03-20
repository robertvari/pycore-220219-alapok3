from game_assets.items import Inventory
import random


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
        self._golds = random.randint(0, 100)
        self._max_weight = 0
        self._inventory = Inventory("Backpack")

        # combat stats
        self._strength = 0
        self._max_HP = 0
        self._current_HP = 0

        self._right_hand = None
        self._left_hand = None

        self._create()

    def _create(self):
        self._name = self.get_fantasy_name()
        self._race = random.choice(list(races))
        self._setup_race()

    def _setup_race(self):
        self._strength = races[self._race]["strength"]
        self._max_HP = races[self._race]["max_HP"]
        self._current_HP = self._max_HP
        self._max_weight = races[self._race]["max_weight"]

    @staticmethod
    def get_fantasy_name():
        FIRST = ['A', 'Ag', 'Ar', 'Ara', 'Anu', 'Bal', 'Bil', 'Boro', 'Bern', 'Bra', 'Cas', 'Cere', 'Co', 'Con',
                 'Cor', 'Dag', 'Doo', 'Elen', 'El', 'En', 'Eo', 'Faf', 'Fan', 'Fara', 'Fre', 'Fro', 'Ga', 'Gala', 'Has',
                 'He', 'Heim', 'Ho', 'Isil', 'In', 'Ini', 'Is', 'Ka', 'Kuo', 'Lance', 'Lo', 'Ma', 'Mag', 'Mi', 'Mo',
                 'Moon', 'Mor', 'Mora', 'Nin', 'O', 'Obi', 'Og', 'Pelli', 'Por', 'Ran', 'Rud', 'Sam', 'She', 'Sheel',
                 'Shin', 'Shog', 'Son', 'Sur', 'Theo', 'Tho', 'Tris', 'U', 'Uh', 'Ul', 'Vap', 'Vish', 'Ya', 'Yo', 'Yyr']

        SECOND = ['ba', 'bis', 'bo', 'bus', 'da', 'dal', 'dagz', 'den', 'di', 'dil', 'din', 'do', 'dor', 'dra',
                  'dur', 'gi', 'gauble', 'gen', 'glum', 'go', 'gorn', 'goth', 'had', 'hard', 'is', 'ki', 'koon', 'ku',
                  'lad', 'ler', 'li', 'lot', 'ma', 'man', 'mir', 'mus', 'nan', 'ni', 'nor', 'nu', 'pian', 'ra', 'rak',
                  'ric', 'rin', 'rum', 'rus', 'rut', 'sek', 'sha', 'thos', 'thur', 'toa', 'tu', 'tur', 'tred', 'varl',
                  'wain', 'wan', 'win', 'wise', 'ya']

        return f"{random.choice(FIRST)}{random.choice(SECOND)}"

    def __repr__(self):
        return self._name

class Player(CharacterBase):
    pass


class Enemy(CharacterBase):
    pass


if __name__ == '__main__':
    enemy1 = Enemy()
    enemy2 = Enemy()
    enemy3 = Enemy()

    pass