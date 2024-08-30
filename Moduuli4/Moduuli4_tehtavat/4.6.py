# Tehtävä 4.6

# Kirjoita ohjelma, joka kysyy arvottavien pisteiden määrän käyttäjältä ja toteuttaa piin likiarvon laskennan.
# Lopuksi ohjelma tulostaa piin likiarvon käyttäjälle.

# π ≈ 4n/N, jossa N on kaikkien pisteiden lukumäärä ja
# n yksikköympyrän sisälle osuvien pisteiden määrä
# jos pisteen koordinaatit (x,y) toteuttavat epäyhtälön x^2+y^2<1, piste on yksikköympyrässä

import random

N = int(input("Syötä arvottavien pisteiden lukumäärä: "))   # kysytään pisteiden kokonaismäärä
n = 0                                                       # ympyrään osuvien pisteiden lkm
iterator = 0
while iterator < N:
    iterator += 1
    x = random.uniform(-1, 1)                            # arvotaan yksi piste (x,y)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:                                     # testataan, onko piste yksikköympyrässä
        n += 1
pii = 4 * int(n) / int(N)                                   # lasketaan piin likiarvo
print(f"Piin likiarvo on {pii}")
