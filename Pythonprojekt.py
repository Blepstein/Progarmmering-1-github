import klasser
import printasaker
import kammare
import random as rand

hp=100
str=0
lvl=0
inventory=["potion","Häxa"]


printasaker.print_början()
spelare = klasser.player (10, 100, 1, inventory)


dorrar = ["Monster", "Kista", "Fälla"]
rand.shuffle(dorrar)
kammartyp=dorrar[0]

while True:
    val= input(f"Hej {printasaker.namn} tryck s för att starta eller i för att se inventory eller e för egenskaper")
    if val=="s":
        print("Test")
    elif val=="i":
        print(inventory)
    elif val=="e":
        spelare.print_egenskaper()
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






