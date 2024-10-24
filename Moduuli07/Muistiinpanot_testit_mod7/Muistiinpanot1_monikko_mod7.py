# Moduuli 7: MONIKKO ()         (moduulissa myös joukko ja sanakirja, niistä seuraavissa
                                #muistiinpanoissa lisää)

"""
-Monikko (tuple) on muuttumaton: siihen ei voi lisätä alkioita eikä siitä voi poistaa alkioita monikon
luonnin jälkeen
-muutoin on kuten lista, monikko määritetään siis etukäteen
-alkion haku indeksin perusteella on monikon tapauksessa nopeampaa (kuin listasta, lista käy kaikki alkiot läpi)

"""
#from calendar import weekday
#weekday
"""
-Monikko kirjoitetaan sulkeilla: viikonpaivat = ()  #toimii myös ilman sulkeita, mutta on selkeämpi niillä
--> koodi on luettavampaa sulkeiden avulla
-Vertaa: listassa on hakasulkeet: viikon_paivat = []

"""

#esim1. lista vs. monikko
my_list = [1, 2, 3, 4, 5, 6]
print(f"Lista on {my_list}")

my_tuple = (1, 2, 3, 4, 5, 6)         # sama kuin:    my_tuple = 1, 2, 3, 4, 5, 6   #käytä kuitenkin sulkeita
print(f"Monikko on {my_tuple}")

my_tuple2 = (1, 2, (3, 4), 5, "kuusi")
print(f"Monikko 2 on {my_tuple2}")

print()

#luetaan ensimmäinen alkio listasta ja monikosta:       #lukeminen on samanlaista, 0. alkio on ensimmäinen
print(my_list[0])
print(my_tuple[0])

print()

#muokataan listaa: eka alkio muutetaan nroksi 0 ja lisätään loppuun 7
#listan sisältöä voi muokata, mutable = muuttuva
my_list[0] = 0                  #muutetaan vain alkion arvo toiseksi, ei tarvitse poistaa 1. jäsentä
print(f"Muokattu lista: {my_list}")
my_list.append(7)
print (f"Muokattu lista: {my_list}")

print()

#monikon arvoja (sisältöä) EI voi muokata eikä sinne voi lisätä uusia alkioita (immutable)
#jos yrittää muokata, ohjelma ei tulosta rivillä 54 listaa, vaan antaa virheilmoituksen
print(my_tuple)

#Monikkoa on tarkoituksenmukaista käyttää tilanteissa, joissa alkioiden jono on luonteeltaan staattinen:
    #tiedetään, että muutoksille ei ole tarvetta ojelman suorituksen aikana (esim. viikonpäivät, kuukaudet)
    #jotka ovat muuttumattomia.

print()
"""
#esim2. viikonpäivien monikko (koodiesimerkki materiaalista):
viikonpaivat = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
jarjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpaiva = viikonpaivat[jarjestysnumero-1]
print (f"{jarjestysnumero}. viikonpäivä on {viikonpaiva}.")

print()

#esim3. sama kuin yllä, mutta termien nimet vaihdettu englanniksi:
weekdays = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
serial_number = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
weekday = weekdays[serial_number - 1]
print(f"{serial_number}. viikonpäivä on {weekday}.")      #järjestysnumerosta tulee vähentää 1, jotta saadaan oikea alkio ulos
"""
print()

# esim4. Monikon läpikäynti: samoin kuin listan - for-toistorakenteen avulla
for i in my_tuple:          # i voi olla mitä tahansa, on vain käytännössä iteraattorin nimi. Esim. "kukka"
    print(i)                #tulostaa vuorotellen jokaisen listan alkion

print()
#esim5. uusi monikko, sen läpikäynti:
my_tuple3 = ("eka", "toka", "kolmas", "neljäs")
print(my_tuple3)

print()

for i in my_tuple3:
    print(i)            #tämä toimii ilman erillistä kierrosmuuttujaa (iterator), i toimii iteraattorina.

#for-toistorakenne käy läpi listan (tai monikon), eikä se tulosta mitään listan ulkopuolista

print()

#Monikon arvojen purku muuttujiin:
fruits = ("sitruuna", "omena", "appelsiini")
(first, second, third) = fruits     #sama kuin: (first, second, third) = ("sitruuna", "omena", "appelsiini")
print(first)
print(f"Listan kolmas hedelmä on {third}")

print()

#rivinvaihdon voi tehdä \n      #eli "new line n"
#Monikon voi antaa funktiolle parametrina - luodaan ensin funktio:
word_list = ("eka", "toka", "kolmas", "neljäs")

def print_tuple(tuple_name):
    for i in tuple_name:
        print(i)
    #tähän ei ole pakko kirjoittaa return - toimii ilman sitä

print_tuple(word_list)       #kutsutaan funktiota
print()
print_tuple(fruits)             #kutsutaan uudella monikolla

print()

#esim. - materiaalista - perinteinen print ilman funktion paluuarvoa (return)
import random

def heitä():
    eka, toka = random.randint(1,6), random.randint(1,6)
    print(f"Nopista tuli {eka} ja {toka}.")

heitä()

print()
#sama, mutta eri tavalla:
def heitä():
    eka = random.randint(1,6)
    toka = random.randint(1,6)
    print(f"Nopista tuli {eka} ja {toka}.")         #ei ole pakko olla return, toimii ilmankin

heitä()

print()
#sama vielä eri tavalla:
def heitä2():
    (eka, toka) = random.randint(1,6), random.randint(1,6)  #tässä tallennetaan eka ja toka monikkoon
    return (eka, toka)

noppa1, noppa2 = heitä2()
print(f"Nopista saatiin {noppa1} ja {noppa2}.")

print()

#testi, monikon purku muuttujiin
hedelmat = ("banaani", "appelsiini", "omena")
print(hedelmat)
(eka, toka, kolmas) = hedelmat
print(eka, toka)
print(kolmas)
print(f"Hedelmiä ovat {eka}, {toka} ja {kolmas}.")
