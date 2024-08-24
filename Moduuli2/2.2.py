# Tehtävä 2.2.
# Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

# ympyrän pinta-alan kaava on pii*r^2 eli math.pi*r**2

import math

r = float(input("Kerro ympyrän säde (cm): "))   #kysytään säde senttimetreinä
area_circle = math.pi*r**2  #lasketaan ympyrän pinta-ala

print(f"Ympyrän pinta-ala on {area_circle:.3f} neliösenttimetriä.")     #rajataan desimaalit kolmeen
