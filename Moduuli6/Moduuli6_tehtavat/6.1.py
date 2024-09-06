# Tehtävä 6.1
# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def random_number():                    #luodaan muuttuja
    number = random.randint(1,6)
    return number

roll = random_number()                 #kutsutaan funktiota 1. kerran, tallennetaan muuttujaan

while (roll != 6):                       #pääohjelma
    print(roll)
    roll = random_number()             #arvotaan uusi luku, kutsutaan funktiota
if (roll == 6):
    print(roll)
