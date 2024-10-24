"""
Alkuehdollinen toistorakenne (while):
-sama ohjelmakoodin osa suoritetaan useampaan kertaan (loop eli silmukka)

-ohjelmointikielten kolme perusperiaatetta: peräkkäisyys, valinnaisuus, toisto.

Python-kielessä on kaksi toistorakennetta:
-alkuehdollinen toistorakenne (while) - tämä opetellaan moduulissa 4
-iteroiva toistorakenne (for) - ei tarvitse osata vielä

while (alku)ehto:
    toistettava lohko

-Alkuehto testataan rakenteeseen tultaessa. Jos ehto on tosi, suoritetaan sisennetty lohko. Aina sisennetyn lohkon suorituksen jälkeen testataan, onko alkuehto yhä voimassa. Jos ON, sisennetty lohko suoritetaan uudestaan. Kun alkuehto on EPÄTOSI, toistorakenne päättyy

Kuten if-ehtolauseessa, while-ehto on lauseke, jonka totuusarvo voidaan laskea. Ehto on siis joko tosi tai epätosi.
-Jos ehto on TOSI (True), sisennetty lohko suoritetaan
-Jos ehto on EPÄTOSI (False), sisennettyä lohkoa ei suoriteta.

While-toistorakenne toimii kuten if-ehtolause, mutta erona on se, että while toistaa silmukkaa aina uudelleen (niin kauan kun ehtolause on tosi)
"""
#esim1. - ohjelma testaa, onko luku alle 10, ja jos on, lisää siihen luvun yksi, kunnes while-ehto on epätosi
number = 0
while (number < 10):
    number += 1     #sama kuin number = number + 1  #lisätään lukuun yksi
    print(number)

#esim2. käyttäjä lopettaa toiston
komento = input("Anna komento: ")   #tämä on "alkukomento, johon ei palata, sillä se on ennen while-silmukkaa.
while komento != "lopeta":      #kun komento ei ole "lopeta", silmukan sisennykset toistuvat
    print(f"Suoritan toiminnon: {komento}")
    komento = input("Anna komento: ")
print("Toiminnot lopetettu.")         #tulostuu silloin, kun käyttäjä syöttää komennoksi "lopeta"

#esim3. vaihteleva määrä toistoja:
#ohjelma heittää kahta noppaa niin kauan, kunnes molemmista tulee kuutonen, tulostaa montako heittoa tarvittiin.

import random

die1 = die2 = throws = 0                #aluksi 0, koska ei ole heitetty kertaakaan
while (die1 != 6) or (die2 != 6):       #lauseke on epätosi silloin, kun mol. nopista saadaan 6. Muuten epätosi.
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    throws += 1                         #sama kuin (heitot = heitot + 1), lisätään lukuun yksi
print(f"Tarvittiin {throws} heittoa.")  #tulostuu, kun while-ehto on epätosi (eli kun saadaan kuutoset).

"""
SISÄKKÄISET TOISTORAKENTEET:
-while-toistorakenteita voidaan asettaa sisäkkäin
"""
#esim4: tulostetaan kertotaulu yhdestä viiteen.

eka = 1
while eka <= 5:
    toka = 1
    while toka <= 5:
        print(f"{eka} kertaa {toka} on {eka*toka:d}")       #mitä tarkoittaa :d - toimii ilman sitäkin?
        toka = toka + 1                                     # :8d tarkoittaa, että tulostaa 8 merk. lev. kenttään
    eka = eka + 1

#esim5. - laajennettu noppatehtävä (esim3.)
#Laajennetaan edellistä kahden nopan heittämisesimerkkiä siten, että ohjelma tulostaa, montako heittokertaa tarvitaan keskimäärin ennen kuin saadaan kaksi kuutosta.

reps = 0                #toistot
sum_throws = 0            #heitot yhteensä
while reps < 100000:

    die1 = die2 = throws = 0
    while (die1 != 6) or (die2 != 6):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        throws += 1
    #print(f"Tarvittiin {throws} heittoa.")
    reps += 1                               #sama kuin reps = reps + 1
    sum_throws = sum_throws + throws

reps_average = sum_throws / reps
print(f"Heitot keskimäärin: {reps_average:6.2f}")       #6 merkkiä pitkään tilaan, 2 desimaalin tarkkuudella

#sama suomeksi / materiaalin esimerkkikoodaus:
import random
toistot = 0
heitot_yhteensä = 0
while toistot < 100000:

    noppa1 = noppa2 = heitot = 0
    while (noppa1!=6 or noppa2!=6):
        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        heitot = heitot + 1
    #print(f"Tarvittiin {heitot:d} heittoa.")
    toistot = toistot + 1
    heitot_yhteensä = heitot_yhteensä + heitot

heitot_keskimäärin = heitot_yhteensä/toistot
print(f"Heitot keskimäärin: {heitot_keskimäärin:6.2f}")

"""
BREAK:
-Break-komennolla (python-kielessä) voi poistua välittömästi toistorakenteesta (while), jonka jälkeen toistoehdon arvoa (while-ehto) ei enää lasketa.
-käyttöä kannattaa välttää, koska se tekee koodista vaikeasti luettavaa
-toistoehto kannattaa lähtökohtaisesti rakentaa siten, että break-lausetta ei tarvita.

"""


