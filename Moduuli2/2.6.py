# Tehtävä 2.6
# Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
# -kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
# -nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

import random

three_first = random.randint(0,9)   #kolminumeroisen koodin luvut väliltä 0..9
three_second = random.randint(0,9)
three_third = random.randint(0,9)

four_first = random.randint(1,6)    #nelinumeroisen koodin luvut väliltä 1..6
four_second = random.randint(1,6)
four_third = random.randint(1,6)
four_fourth = random.randint(1,6)

print(f"Kolminumeroinen koodi on {three_first} {three_second} {three_third}.")
print(f"Nelinumeroinen koodi on {four_first} {four_second} {four_third} {four_fourth}.")
