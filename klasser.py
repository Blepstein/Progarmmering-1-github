class inventory:
    def inven (self,name, attribute, strengh_bonus):
        self.name = name
        self.attribute = attribute
        self.strengh_bonus = strengh_bonus


class player:
    def __init__(self,strengh, hp, inventory, level):
        self.strengh = strengh
        self.hp = hp
        self.inventory = inventory
        self.level = level

    def print_egenskaper(self):
        print(f"Du har {self.strengh} strengh och {self.hp} hp har {self.inventory} inventory och är på {self.level} level")

class monster:
    