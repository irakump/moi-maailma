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
