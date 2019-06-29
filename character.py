import random
from math import ceil
from weapons import Weapon


class Character:
    """Character class. Instances have hp, accuracy, attack, damage and defense
    attributes. They also have a punch method"""
    def __init__(self, name, level=1, hp=20, accuracy=50,
                 attack=2, defense=2, dodge=0, weapon=None, armor=None):
        super(Character, self).__init__()
        self.name = name
        self.level = level

        # Character's stats
        self.hp = hp
        self.accuracy = accuracy
        self.attack = attack
        self.defense = defense
        self.dodge = 2 + dodge
        self.weapon = weapon
        self.armor = armor

    @property
    def protection(self):
        if self.armor == None:
            return self.defense
        else:
            return self.defense + self.armor.defense

    @property
    def damage(self):
        if self.weapon == None:
            return self.attack
        else:
            return self.attack + self.weapon.damage

    def level_up(self):
        """Increments the character's level and increases its stats """
        self.level += 1
        self.hp = ceil(self.hp * 1.1)
        self.defense = ceil(self.defense * 1.2)
        self.attack = ceil(self.attack * 1.2)
        # Accuracy increased every 3 levels
        if self.level % 3 == 0:
            self.accuracy = ceil(self.accuracy * 1.2)

    def punch(self, target):
        """Takes into account accuracy and dodge for probability of hit.
        Takes self's 'damage' and target's 'defense' attributes to return damage inflicted by the punch
        Side effect : prints a string with end result."""
        roll = random.randint(1, 100)
        if roll < self.accuracy - target.dodge:
            damage = self.damage - target.protection
            if damage < 0:
                damage = 0
            target.hp -= damage
            print(f"{target.name} is hit : {damage} dmg")
        else:
            print("Missed")

if __name__ == "__main__":
    player1 = Character("Billy")
    player2 = Character("Joe")
    for _ in range(10):
        player1.level_up()
        print(
            f"""lvl: {player1.level},\
            def: {player1.defense},\
            protection: {player1.protection}"""
            )

