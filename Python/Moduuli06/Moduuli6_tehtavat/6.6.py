# Tehtävä 6.6
# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa
# paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

def count_price_per_square_meter(diameter, price):          #funktion parametreina halkaisija, hinta
    area = math.pi * ((diameter*0.01) / 2)**2               #lasketaan pizzan pinta-ala neliömetreinä
    result = (price / area)                                 #lasketaan pizzan hinta per neliömetri
    return result

#kysytään ja tallennetaan 1. pizzan tiedot
user_input_diameter1 = float(input("Kerro ensimmäisen pizzan halkaisija (cm): "))
user_input_price1 = float(input("Kerro ensimmäisen pizzan hinta (€): "))
diameter1 = user_input_diameter1
price1 = user_input_price1

#kysytään ja tallennetaan 2. pizzan tiedot
user_input_diameter2 = float(input("Kerro toisen pizzan halkaisija (cm): "))
user_input_price2 = float(input("Kerro toisen pizzan hinta (€): "))
diameter2 = user_input_diameter2
price2 = user_input_price2

best_unit_price = 0                                         #luodaan muuttuja, alhaisempi yksikköhinta

#lasketaan funktiolla pizzojen yksikköhinnat ja ilmoitetaan tulos (alhaisempi yksikköhinta)
pizza1 = (count_price_per_square_meter(diameter1, price1))
best_unit_price = pizza1                                    #tallennetaan yksikköhinta muuttujaan
pizza2 = (count_price_per_square_meter(diameter2, price2))
if pizza2 < best_unit_price:
    best_unit_price = pizza2 = "pizza 2"                    #tallennetaan muuttujaan ja muutetaan merkkijonoksi
else:
    best_unit_price = "pizza 1"
print(f"Alhaisempi yksikköhinta: {best_unit_price}")
