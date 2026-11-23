import klasser
import random as rand

hp=100
str=0
lvl=0
inventory=["potion","Häxa"]

class Player:
    def __init__(self,strengh, hp, inventory, level):
        self.strengh = strengh
        self.hp = hp
        self.inventory = inventory
        self.level = level

    def print_egenskaper(self):
        print(f"Du har {self.strengh} strengh och {self.hp} hp har {self.inventory} inventory och är på {self.level} level")
    

#FÖR KISTOR OCH FÄLLOR
frukter = ["Äpple", "Banan", "Drakfrukt"]
# Äpple har vikt 70, Banan 25, Drakfrukt 5 (totalt 100)
resultat = random.choices(frukter, weights=[70, 25, 5], k=1)

print(f"Du hittade en {resultat[0]}!")


print("Detta är ett textbaserat äventyrsspel där du navigerar genom kammare i slott, samlar på dig föremål och slåss mot monster")
namn=input("Vad vill du heta under spelens gång?")

spelare = Player(str, hp, inventory, lvl)
spelare.print_egenskaper()


#printa egnskaper + inventory

import random

dorrar = ["Monster", "Kista", "Fälla"]
random.shuffle(dorrar)

while True:
    try:
        kammare = int(input("Välj mellan kammare 1 2 eller 3 "))

        if kammare == 1 or kammare == 2 or kammare == 3:
            break
        else:
            continue

    except:
        print("Något är fel")
<<<<<<< HEAD
=======

print("Bakom dörren finns:", dorrar[kammare - 1])
>>>>>>> c33b3a396f119b62a69a24bd7e0df9e8dec0a7eb
