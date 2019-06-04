import random


class Spell:
    def __init__(self, name, cost, dmg, cty):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.cty = cty

    def generate_magic_dmg(self):
        if self.cty == 'BlackMagic':
            dmgl = self.dmg - 10
            dmgh = self.dmg + 10
            return random.randrange(dmgl, dmgh)
        elif self.cty == 'WhiteMagic':
            return self.dmg
