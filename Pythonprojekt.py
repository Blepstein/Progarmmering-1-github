import klasser
import random as rand
import text

text.print_title()

hp=100
str=0
lvl=0
inventory=["potion","Häxa"]


print("Detta är ett textbaserat äventyrsspel där du navigerar genom kammare i slott, samlar på dig föremål och slåss mot monster")
namn=input("Vad vill du heta under spelens gång?")

spelare = klasser.player (9, 100, 6, 7)
spelare.print_egenskaper()

#printa egnskaper + inventory


dorrar = ["Monster", "Kista", "Fälla"]
rand.shuffle(dorrar)
kammartyp=dorrar[0]

while True:
    input(f"Hej {namn} tryck s för att starta eller i för att se inventory")
    while True:
        try:
            kammare = int(input("Välj mellan kammare 1 2 eller 3 "))

            if kammare == 1 or kammare == 2 or kammare == 3:
                break
            else:
                print("Skriv 1 2 eller 3")
                continue
        except:
            print("Något är fel")




print("Bakom dörren finns:", dorrar[kammare - 1])

