hp=0
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
    

player_egenskaper = Player(10,100,[],0)

player_egenskaper.print_egenskaper()


print("Detta är ett textbaserat äventyrsspel där du navigerar genom kammare i slott, samlar på dig föremål och slåss mot monster")
namn=input("Vad vill du heta under spelens gång?")



#printa egnskaper + inventory

while True:
    try:
        kammare=int(input("Välj mellan kammare 1 2 eller 3"))
        if kammare==1 or kammare==2 or kammare==3:
            break
        else:
            continue
    except:
          print("Något är fel")



import random

kammar.typ = ["monster", "skatt", "fälla",]
fortsatt = True

while fortsatt:
    svar = input("Välj ett alternativ, 1, 2 eller 3 (eller 'q' för att sluta): ")
    
    if svar == "q":
        fortsatt = False
    else:

