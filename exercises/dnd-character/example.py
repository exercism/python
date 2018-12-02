import random
import math


class Character:
    character = {}

    def __init__(self):
        self.character = {
            'strength': self.ability(),
            'dexterity': self.ability(),
            'constitution': self.ability(),
            'intelligence': self.ability(),
            'wisdom': self.ability(),
            'charisma': self.ability()
            }
        self.character['hitpoints'] = 10 + self.modifier(
                    self.character['constitution'])

    def ability(self):
        return random.randint(3, 18)

    def modifier(self, value):
        return math.floor((value-10)/2)
