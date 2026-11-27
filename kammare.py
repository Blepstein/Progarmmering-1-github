import klasser
import Pythonprojekt
import random as rand
def fälla():
    # if kammartyp == "fälla":
    hp -= rand.randint(10,30)
    print(f"Du stötte på en fälla och har kvar {hp} hp")



svärd = klasser.inventory ("svärd",0,10)
dolk = klasser.inventory ("dolk",0,10)


#if klasser.kammartyp == "kista":
def kista():
    #FÖR KISTOR OCH FÄLLOR
    frukter = ["Äpple", "Banan", "Drakfrukt"]
    # Äpple har vikt 70, Banan 25, Drakfrukt 5 (totalt 100)
    resultat = rand.choices(frukter, weights=[70, 25, 5], k=1)
    Pythonprojekt.inventory.append(resultat)
    print(f"Du hittade en {resultat[0]}!")
    #om kistans items är mer än fem ska man behöva byta ut den

# #FÖR KISTOR OCH FÄLLOR
# frukter = ["Äpple", "Banan", "Drakfrukt"]
# # Äpple har vikt 70, Banan 25, Drakfrukt 5 (totalt 100)
# resultat = random.choices(frukter, weights=[70, 25, 5], k=1)

monster = ""
def monster_fight():
#while hp > 0:
#Det ska väl inte vara hp-1 ibörjan
    hp = hp - 1
    if str < monster:
        print('Monstret slog ner dig!')
    elif str == monster:
        print('Oavgjort')
    else:
        print('Du slog ner monstret!')