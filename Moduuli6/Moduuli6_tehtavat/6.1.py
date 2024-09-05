# Tehtävä 6.1
# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def random_number():
    random.randint(1,6)
    return

number = random_number()
print(number)

"""
while number != 6:
    print(number)
    random_number()
"""
#for die in dice:
#    print(random_number())

