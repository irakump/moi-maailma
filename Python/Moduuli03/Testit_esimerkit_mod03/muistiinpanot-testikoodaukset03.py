#viikko 2 - valintarakenne (mod03) ja while-toistorakenne (mod04)

#pycharmissa ylhäällä on leppäkerttu-symboli: DEBUG. Paina numeron kohdalle pun. ympyrä (stop)
#näyttää koodissa, mitkä muuttujat on tallennettu (string = merkkijono)

#soft-wrap-painikkeella (hiiren oikea numeroiden kohdalla) saa tekstin rivitettyä paremmin, jos pitkä teksti

#AI-ominaisuuden saa pois: settings - plugins (niin ei anna automaattisesti ehdotuksia koodia kirjoittaessa) - käynnistä sen jälkeen pycharm uudelleen

#myöhemmin opetellaan virheenkäsittelyä (jos joku laittaa kirjaimia, kun pyydetään numeroita), ei tarvitse vielä osata

#PELKÄN KOKONAISOSAN PALAUTTAVA JAKOLASKU: //   (jakolasku, josta tulee kokonaisluku tulokseksi)

#JAKOJÄÄNNÖSOPERAATIO: %

#######################################

#Mod03 VALINTARAKENNE (IF)

#ehto: jos rahaa_taskussa>=5   #yhtä paljon tai enemmän kuin 5
# osta latte

#if-ehto = tehdään jotakin

'''Loogiset operaattorit: and, or, not

true/false on boolean-arvo (ei merkkijono eikä luku)

materiaaleissa read.me-tiedosto, jossa kuva if-ehdosta




'''
#print(1==1)     #true
##print(1 != 1)   #false
#print(not 1 != 1)   #true

#print(True)     #boolean-komennot?: tulee olla iso alkukirjain

#print(True and True)    #True
#print(f"Vertailun tulos: {result}")

#print(1 == 2 or 1 == "1")
#print(1 < 2 or (1 ==1 and result == True))
#print(" ")

#jos on epävarma esim. tentissä, tee välitulostus, niin näkee mikä on tuloste (esim. True), eli toimiiko koodi oikein/siten miten halutaan

#While-silmukat (loopit):
#while True:         #ikuinen silmukka --> jossakin vaiheessa loopin tulee päättyä!
#    print("Moi")
#    print("Ira")

#laskuri:
#counter = 0
#while counter < 5:
#    print(f"{counter}. kerran moi")
#    counter = counter + 1   #tässä tehdään sijoitus vanhan arvon päälle, eli counter ei enää ole 0. Seuraavalla loopilla +1, ja taas +1...
#print(f"Laskurin arvo lopuksi: {counter}")  #lopettaa toimintansa, kun arvo on enmmän kuin 5.

#laskuri2: halutaan, että laskurin arvo on lopussa 5, ja tulostaa luvut 1,...5
"""
print("laskuri nro 2")
counter = 0
while counter < 5:
    print(f"{counter}. kerran moi")
    counter = counter + 1
print(f"Laskurin arvo lopuksi: {counter}")      #vertaa tätä laskuriin 3 :
print(" ")

#laskuri3:
print("Laskuri nro 3")
counter = 0
while counter < 5:      #tähän voi laittaa, montako kertaa haluaa loopin toistuvan, nyt toistuu 5 kertaa.
    counter = counter + 1
    print(f"{counter}. kerran moi")
print(f"Laskurin arvo lopuksi: {counter}")
print(" ")

#ehto: jos ei toteudu, niin loopia ei toisteta. Jos toteutuu (True), niin toistetaan.

#laskuri4:
print("Laskuri nro 4")

max_count = int(input("Montako kertaa moikataan? "))
counter = 0
while counter < max_count:      #tähän voi laittaa, montako kertaa haluaa loopin toistuvan,
    counter = counter + 1
    print(f"{counter}. kerran moi")
print(f"Laskurin arvo lopuksi: {counter}")

print(" ")
"""
"""
#ohjelma komentorivikäyttöliittymällä
command = input("Komento, kiitos> ")
if command == "lopeta":
    print("Lopetetaan.")
else:       #komento on joku muu kuin lopeta
    print("En ymmärrä komentoa. Yritä uudestaan, kiitos.")  #ohjelma loppuu, koska ei ole while-silmukkaa (looppia)

print(" ")

#ohjelma uudestaan:
while True:     #while True on huono tapa (myöhemmin opetetaan parempi)     #kannaattaa lukea, montako kertaa silmukka toistuu
    command = input("Komento, kiitos> ")
    if command == "lopeta":
        print("Lopetetaan.")
        #break           # "heittää ulos" loopista, eli tästä hyppää riville 113. Ei paras ohjelmointikäytäntö.
    else:            #komento on joku muu kuin lopeta
        print("En ymmärrä komentoa. Yritä uudestaan, kiitos.")
print("Ohjelma sammutettu.")

print(" ")
"""
"""
#parempi ohjelma
command = ""
while command != "lopeta":      #niin kauan kuin komento ei ole lopeta, ohjelmaa suoritetaan. Tämä on parempi kuin yllä oleva tapa
    command = input("Komento, kiitos> ")
    if command == "lopeta":
        print("Lopetetaan.")
        #break           # "heittää ulos" loopista, eli tästä hyppää riville 113. Ei paras ohjelmointikäytäntö.
    elif command == "moi":
        max_count = int(input("Montako kertaa moikataan? "))        #tähän kopioitu aikaisempi ohjelma
        counter = 0
        while counter < max_count:  # tähän voi laittaa, montako kertaa haluaa loopin toistuvan,
            counter = counter + 1
            print(f"{counter}. kerran moi")
        print(f"Laskurin arvo lopuksi: {counter}")
    else:            #komento on joku muu kuin lopeta
        print("En ymmärrä komentoa. Yritä uudestaan, kiitos.")
print("Ohjelma sammutettu.")
"""

#noppasimulaattori (import random): kuinka monta kertaa noppaa pitää heittää, että tulee nro 6? satunnainen, keskimäärin joka 6. heitto on luku 6.
#tulee tehdä muuttuja, joka laskee heittojen lukumäärän.

import random   #laita tämä koodissa tiedoston alkuun (riville 1)
"""
die1 = 0    #alkuun laitetaan joku luku, joka poikkeaa nopan silmäluvuista
roll_counter = 0        #laskuri heittoihin
while die1 < 6:    #loop pyörii niin kauan, kunnes luku on 6.
    roll_counter += 1
    die1 = random.randint(1,6)      #die=noppa?
    print(f"{roll_counter}. heiton silmäluku on {die1}.")   #tämän voi jättää kommenttiin, jos haluaa tulosteeksi vain, kuinka monennella heitolla tulee luku 6.
print(f"Noppaa heitettiin {roll_counter} kertaa.")
"""

"""
#noppasimulaattori2: kaksi noppaa, kuinka monesti heitetään, jotta tulee molemmista luku 6.
die1 = 0    #alkuun laitetaan joku luku, joka poikkeaa nopan silmäluvuista
die2 = 0
roll_counter = 0        #nämä voisi sijoittaa samalle riville: die1 = die2 = roll_counter = 0

while die1 < 6 or die2 < 6:    #loop pyörii niin kauan, kunnes luku on 6.
    roll_counter += 1
    die1 = random.randint(1,6)      #die=noppa?
    die2 = random.randint(1,6)
    print(f"{roll_counter}. heiton silmäluvut: {die1} ja {die2}.")   #tämän voi jättää kommenttiin, jos haluaa tulosteeksi vain, kuinka monennella heitolla tulee luku 6.
print(f"Noppaa heitettiin {roll_counter} kertaa.")
"""

#noppasimulaattori3:
#mikä on kahden yhtäaikaisen kutosen todennäköisyys? (laskemalla 1/36)

rounds = 1000             #montako kierrosta pelattu
round_counter = 0       #montako kierrosta tehty, aloitetaan luvusta 0
total_rolls = 0

while round_counter < rounds:
    round_counter += 1      #joka kierroksella lisätään 1 kierroksiin
    die1 = 0    #alkuun laitetaan joku luku, joka poikkeaa nopan silmäluvuista
    die2 = 0
    roll_counter = 0        #nämä voisi sijoittaa samalle riville: die1 = die2 = roll_counter = 0
    while die1 < 6 or die2 < 6:    #loop pyörii niin kauan, kunnes luku on 6.
        roll_counter += 1
        die1 = random.randint(1,6)      #die=noppa
        die2 = random.randint(1,6)
        #print(f"{roll_counter}. heiton silmäluvut: {die1} ja {die2}.")   #tämän voi jättää kommenttiin, jos haluaa tulosteeksi vain, kuinka monennella heitolla tulee luku 6.
    #print(f"Noppaa heitettiin {roll_counter} kertaa.")
    total_rolls = total_rolls + roll_counter    #lisätään heitetyt kierrokset
print(f"Kaksi kutosta saatiin keskimäärin {total_rolls / rounds} heitolla/kierros") #tässä on samalla laskukaava, lasketaan heittojen lukumäärä kierroksilla? (nyt kierroksia 10, ks. muuttuja rounds (aiemmin oli rounds = 10)

#jos laittaa enemmän kierroksia, esim. 100 000, tulee lähemmäksi todennäköisyyttä 1/36

#tämän voi yhdistää aiempaan komentorivikäyttöliittymään (elif-toiminnolla):
command = ""
while command != "lopeta":      #niin kauan kuin komento ei ole lopeta, ohjelmaa suoritetaan. Tämä on parempi kuin yllä oleva tapa
    command = input("Komento, kiitos> ")
    if command == "lopeta":
        print("Lopetetaan.")
        #break           # "heittää ulos" loopista, eli tästä hyppää riville 113. Ei paras ohjelmointikäytäntö.
    elif command == "moi":
        max_count = int(input("Montako kertaa moikataan? "))        #tähän kopioitu aikaisempi ohjelma
        counter = 0
        while counter < max_count:  # tähän voi laittaa, montako kertaa haluaa loopin toistuvan,
            counter = counter + 1
            print(f"{counter}. kerran moi")
        print(f"Laskurin arvo lopuksi: {counter}")
    elif command == "noppa":
        rounds = 1000  # montako kierrosta pelattu
        round_counter = 0  # montako kierrosta tehty, aloitetaan luvusta 0
        total_rolls = 0

        while round_counter < rounds:
            round_counter += 1  # joka kierroksella lisätään 1 kierroksiin
            die1 = 0  # alkuun laitetaan joku luku, joka poikkeaa nopan silmäluvuista
            die2 = 0
            roll_counter = 0  # nämä voisi sijoittaa samalle riville: die1 = die2 = roll_counter = 0
            while die1 < 6 or die2 < 6:  # loop pyörii niin kauan, kunnes luku on 6.
                roll_counter += 1
                die1 = random.randint(1, 6)  # die=noppa
                die2 = random.randint(1, 6)
            total_rolls = total_rolls + roll_counter  # lisätään heitetyt kierrokset
        print(f"Kaksi kutosta saatiin keskimäärin {total_rolls / rounds} heitolla/kierros")
    else:            #komento on joku muu kuin lopeta
        print("En ymmärrä komentoa. Yritä uudestaan, kiitos.")
print("Ohjelma sammutettu.")

#break-komentoa ei kannata käyttää (jos löytyy parempi tapa), eli muotoile ehto siten, että tiedetään milloin silmukka/loop päättyy.

muuttuja = 0
muuttuja  = muuttuja + 1 #muuttujaan lisätään luku 1. sama lyhyemmin: counter =+ 1

#tulostetaan luvun 2 potenssit:
x = 2
while x < 1000:     #max 1000 asti
    print(x)
    x = x * 2   #sama tulos, lyhyempi koodi: x *= 2

#to 29.8. tunnilla tehdään tehtäviä (voi kysyä apua), ei tule uutta opetusta.

"""
Tapa selvittää, onko luku int vai float:
You can get the type of an object with the built-in type() function.
i = 100
f = 1.23

print(type(i))
print(type(f))
# <class 'int'>             #tulosteet: i on kokonaisluku, joten tulostuu <class 'int'>
# <class 'float'>           #           f liukuluku, joten tulostuu <class 'float'>

##########################
Check if float is an integer: is_integer()
f = 1.23

print(f.is_integer())
# False

f_i = 100.0

print(f_i.is_integer())
# True

"""