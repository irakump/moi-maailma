# if-ehto

#esim. 1: laten osto, jos on tarpeeksi rahaa
money = float(input("Kerro rahamäärä: "))
if money >= 5:              #jos tämä ehto toteutuu, tulostuu rivi 5. Jos ei toteudu, ei                                  tapahdu mitään.
    print("Voit ostaa latten.")

"""
Vertailuoperaattorit: 
> suurempi kuin
< pienempi kuin
>= suurempi tai yhtä suuri kuin
<= pienempi tai yhtä suuri kuin
== yhtä suuri kuin
!= eri suuri kuin

Loogisia operaattoreita voi ketjuttaa: esim. 2 < 5 < 8

Operaattoreita voi käyttää myös merkkijonoilla: m1 < m2 on tosi silloin, kun merkkijono m1 on aakkosjärjestyksessä ennen merkkijonoa m2
"""

#Aakkosjärjestyksen testaus:
a = "Aatami"
b = "Bertta"

print(a < b)    #tulostaa true, koska a on ennen b:tä aakkosissa (a silloin pienempi)


#esim. 2: merkkijonojen yhtäsuuruus (== -merkki)
suutari = input("Kerro suutarin nimi: ")
raatali = input("Kerro räätälin nimi: ")
if suutari == raatali:      #jos suutarilla ja räätälillä on sama nimi, toteutuu rivi 33.
    print("Suutarilla ja räätälillä on sama nimi!")
else:
    print(f"Suutarin nimi on {suutari} ja räätälin nimi on {raatali}.")

"""
Loogiset operaattorit:
and (ja = molemmat toteutuvat)
or (tai = jompikumpi tai molemmat)
not (ei = negaatio)

Operaattorien avulla voidaan yhdistää ehtoja toisiinsa. 
"""

#esim. 3: voiko lääkettä antaa potilaalle
"""
Ohjelma ilmoittaa, jos lääkettä saa antaa potilaalle. Lääkkeen käyttö on sallittua, kun potilas on aikuinen. Käyttö on sallittua myös, jos potilas on vähintään 15-vuotias ja hänen painonsa on vähintään 55 kiloa. Seuraava ohjelma kysyy aluksi potilaan iän. Jos ikä on vähintään 15 mutta alle 18 vuotta, ohjelma kysyy myös painon. Lopuksi ohjelma ilmoittaa käyttäjälle, jos lääkkeen käyttö on sallittua.
"""
age = int(input("Kerro ikäsi: "))
if 15 <= age < 18:
    weight = float(input("Kerro painosi (kg): "))
if (age >= 18 or (age >= 15 and weight >= 55)):  #sulkeet ei pakolliset (and), mutta selkeyttää
    print("Voit käyttää lääkettä.")

#Kaksi toisensa poissulkevaa vaihtoehtoa: if ja else
"""
if (ehto):
    lohko, joka suoritetaan, jos ehto on tosi
else:
    lohko, joka suoritetaan, jos ehto on epätosi
"""

#esim3: parempi tapa, lisätään else-haara:  (edellinen esimerkki ei tulostanut mitään, jos alle 15v)

age = int(input("Kerro ikäsi: "))
if 15 <= age < 18:
    weight = float(input("Kerro painosi (kg): "))
if (age >= 18 or (age >= 15 and weight >= 55)):  #sulkeet ei pakolliset (and), mutta selkeyttää
    print("Voit käyttää lääkettä.")
else:
    print("Et saa käyttää lääkettä.")

# jos on enemmän kuin kaksi vaihtoehtoa, käytetään elif-komentoa (MONTA VAIHTOEHTOA):
#esim 4: ikäkysely
ikä = int(input("Anna ikäsi: "))
if ikä>=65:
    print("Olet eläkeiässä.")
elif ikä>=18:
    print("Olet työiässä.")
elif ikä>=7:
    print("Olet koululainen.")
else:
    print("Olet pikkulapsi.")

#esimerkissä 4 käydään ehto kerrallaan läpi, ylimmästä alkaen. Yläikärajaa ei tarvitse määrittää, koska tiedetään, että edellinen ehto ei toteutunut (esim. ikä 40: ehto ikä >=65 on epätosi, jolloin siirrytään seuraavaan ehtoon.
