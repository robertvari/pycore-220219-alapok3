from game_assets.items import Inventory, Weapon, Food, Cloth
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
        self.inventory = Inventory("Backpack")

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

    def add_item(self, item):
        if isinstance(item, Weapon) and not self._right_hand:
            self._right_hand = item

        self.inventory.add_item(item)

    def attack(self, other):
        print(f"{self._name} attacks {other}")

        attack_strength = random.randint(0, self._strength)

        if attack_strength == 0:
            print(f"{self._name} misses {other}")
        else:
            print(f"{self._name} hits {other} with {attack_strength} strength")
            other.apply_damage(attack_strength)

    def apply_damage(self, damage):
        self._current_HP -= damage

    @property
    def alive(self):
        return self._current_HP > 0

    def loot(self, other):
        print(f"{self._name} won the fight.")

        other_items = other.inventory.get_items()
        for item in other_items:
            self.inventory.add_item(item)

        other.inventory.clear()

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
    def _create(self):
        self._name = input("What is your name?")
        result = input(f"What is your race? {list(races)}")
        while result not in list(races):
            result = input(f"What is your race? {list(races)}")

        self._race = result
        self._setup_race()


class Enemy(CharacterBase):
    pass


if __name__ == '__main__':
    enemy = Enemy()

    common_sword = Weapon("Common Sword", 10, 34)
    bread = Food("Bread", 3, 7)
    enemy.add_item(common_sword)
    enemy.add_item(bread)

    player = Player()
    player.add_item(bread)

    while True:
        enemy.attack(player)

        if not player.alive:
            print(f"{player} is dead :(")
            enemy.loot(player)
            break

        player.attack(enemy)

        if not enemy.alive:
            print(f"{enemy} is dead")
            player.loot(enemy)
            break

