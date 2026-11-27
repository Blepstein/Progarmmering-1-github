import klasser
import printasaker
import kammare
import random as rand
import text


hp=100
str=0
lvl=0
inventory=["potion","Häxa"]

text.print_title()
spelarens_namn = printasaker.print_början()
spelare = klasser.player (str, hp, inventory, lvl)


dorrar = ["Monster", "Kista", "Fälla"]
rand.shuffle(dorrar)
kammartyp=dorrar[0]

while True:
    while True:
        val= input(f"Hej {spelarens_namn} tryck s för att starta eller i för att se inventory eller e för egenskaper")
        if val=="s":
            break
        elif val=="i":
            print(inventory)
        elif val=="e":
            spelare.print_egenskaper()
        else:
            print("Skriv s i eller e")

    while True:
        try:
            kammare = int(input("Välj mellan kammare 1 2 eller 3 "))

            if kammare == 1 or kammare == 2 or kammare == 3:
                break
            else:
                print("Skriv 1 2 eller 3")
                continue
        except:
            print("Skriv 1 2 eller 3 med siffror")
    print("Bakom dörren finns:", dorrar[kammare - 1])
    if kammartyp=="Monster":
        kammare.monster_fight()
    elif kammartyp=="Fälla":
        kammare.fälla()
    elif kammartyp=="Kista":
        kammare.kista()






