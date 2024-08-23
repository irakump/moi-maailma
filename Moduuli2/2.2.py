# Tehtävä 2.2.
# Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

#ympyrän pinta-alan kaava on pii*r^2 eli math.pi*r**2

import math

r = input("Kerro ympyrän säde: ")
area_circle = math.pi*float(r)**2   #muuttuja r on merkkijono, muutos liukuluvuksi
print("Ympyrän pinta-ala on " + str(area_circle))   #liukuluvun muutos merkkijonoksi

#saman tulosteen saa myös seuraavalla: print(f"Ympyrän pinta-ala on {area_circle}")