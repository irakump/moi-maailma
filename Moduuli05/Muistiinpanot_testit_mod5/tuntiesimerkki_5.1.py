#tehtävä 5.1 on tarkoitus tehdä kokonaan for-silmukan avulla (ilman listaa!)

import random
total = int(input("Kerro noppien lukumäärä: "))
die_sum = 0

for i in range (total):
    die = random.randint(1, 6)
    die_sum = die_sum + die
print(f"Noppien silmälukujen summa on {die_sum}.")

#koodia tehdessä on nopeampi testata, kun "kovakoodaa" arvon, eli laittaa esi. total = 5,
#ja kun koodi toimii, voi sen muuttaa inputiksi, jolla kysyy käyttäjältä arvon

#toinen tapa - listan avulla:

total2 = int(input("Kerro noppien lukumäärä: "))
results = []

for i in range (total2):
    result = random.randint(1, 6)
    results.append(result)
print(f"Noppien silmälukujen summa on {sum(results)}.")
