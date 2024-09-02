# Tehtävä 5.1
# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

import random
iterator = 0                            #kierrosmuuttuja
dices = []                              #tyhjä lista noppien silmälukuja varten

number = int(input("Syötä arpakuutioiden lukumäärä: "))

while iterator < number:
    dice = random.randint(1,6)
    dices.append(dice)                  #lisätään nopan silmäluku listaan
    iterator += 1                       #kasvatetaan kierrosmuuttujaa

sum = 0

for dice in dices:
    sum = sum + dice                     #lisätään nopan silmäluku summa-muuttujaan
print(f"Silmälukujen summa on {sum}.")
