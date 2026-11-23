import klasser
import Pythonprojekt
import random as rand

if kammartyp == "fälla":
    hp-=rand.randint(10,30)
    print(f"Du stötte på en fälla och förlora {hp} hp")
    continue


svärd = inventory ("svärd",0,10)
dolk = inventory ("dolk",0,10)


if kammartyp == "kista":
    inventory.append[""]

#FÖR KISTOR OCH FÄLLOR
frukter = ["Äpple", "Banan", "Drakfrukt"]
# Äpple har vikt 70, Banan 25, Drakfrukt 5 (totalt 100)
resultat = random.choices(frukter, weights=[70, 25, 5], k=1)