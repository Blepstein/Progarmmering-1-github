import klasser
import random as rand

hp=100
str=0
lvl=0
inventory=["potion","Häxa"]

print("Detta är ett textbaserat äventyrsspel där du navigerar genom kammare i slott, samlar på dig föremål och slåss mot monster")
namn=input("Vad vill du heta under spelens gång?")

spelare = klasser.player(str, hp, inventory, lvl)
klasser.player(str, hp, inventory, lvl)


print(f"Dina items i inventory är {inventory}")
while True:
    try:
        kammare=int(input("Välj mellan kammare 1 2 eller 3 "))
        if kammare==1 or kammare==2 or kammare==3:
            break
        else:
            continue
    except:
        print("Något är fel")

print("Hej")


if kammartyp == "fälla":
    hp-=rand.randint(10,30)

if kammartyp == "kista"