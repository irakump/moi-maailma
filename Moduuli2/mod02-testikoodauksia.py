# Tehtävä 2.2.: Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
# ympyrän pinta-ala: pii*r^2

r = float(input("Anna ympyrän säde (m): ")) #voi nimetä esim. ympyran_sade tai r.

3.14 * r**2     #kaksi tähteä on potenssi

import math

area = math.pi * r**2
# print(area) #tässä tulee liukuluku.
# print(f"Ympyrän, jonka säde on {r}, pinta-ala on {area} neliömetriä.") #tässä liukuluku.

#ei liukulukua:
print(f"Ympyrän, jonka säde on {r}, pinta-ala on {area:.1f} neliömetriä.")

#väliviivaa ei voi käyttää muuttujien nimessä, koska se on miinus matematiikassa.
#toisella koodausohjelmalla voi käyttää esim. ympyranSade (pythonissa käytetään alaviivaa)
#työelämässä muuttujat nimetään aina englanniksi, esim. circle_radius
#nimeä muuttujat siten, että kuvaavat, mikä arvo on kyseessä.

#2.5-tehtävässä voi hyödyntää jakojäännöstä.

import random

#random.randint() -funkio, tutustu sen käyttöön (arvontatehtävät, esim. 2.6)

#satunnaisen kokonaisluvun arpominen väliltä 1-6:
random_number = random.randint (1, 6) #tallenna johonkin muuttujaan random.randint.
#a ensimmäinen luku ja viimeinen, eli miltä väliltä luvut arvotaan.
print(f"Satunnainen luku 1-6: {random_number}")

#kaikki importit aina tiedoston ylös
