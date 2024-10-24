# SANAKIRJA {} eli dictionary

#Sanakirja on Pythonin käytetyimpiä tietorakenteita.
#Sanakirjaan voidaan tallentaa avain-arvopareja, esim. nimi ja puhelinnumero, nimi toimii avaimena

#Sanakirja-tietorakenteesta käytetään toisinaan nimityksiä assosiatiivinen taulukko ja hajautusrakenne.

#Sanakirja alustetaan luettelemalla arvot - annetaan kukin avain-arvopari seuraavasti: avain : arvo.
#Peräkkäiset avain-arvoparit erotellaan toisistaan pilkuilla.

#Alustetaan sanakirja, jossa avain on oppilaan nimi ja arvo on oppilaan ikä
oppilaat = {"Aapeli" : 25, "Bertta" : 19, "Cecilia" : 41, "Daniel" : 9, "Emma" : 31}
print(oppilaat)

print()
#tutkitaan, mitä ovat tietueet eli items (tätä ei ole materiaalissa) - item = avain-arvopari (yhdessä):
print(oppilaat.items())

print()
#tutkitaan, mitä ovat sanakirjan AVAIMET:
print(oppilaat.keys())              #key = avain

#sanakirjan ARVOT:
print(oppilaat.values())            #arvo = value

print()

#Kun sanakirjaa käydään läpi for/in -rakenteella:

#tietueet eli avain-arvopari (items) - tulostetaan tietueet yksitellen:
for i in oppilaat.items():
    print(i)

print()

#Kun sanakirja läpikäydään for/in-rakennetta käyttäen,
#saa kierrosmuuttuja arvokseen vuoron perään kunkin sanakirjassa esiintyvän avaimen.

for i in oppilaat:      #eli ei tarvitse olla oppilaat.items !
    print(i)

##########
print()
##########

#Yksittäisen arvon haku avaimen avulla (tässä haetaan Aapelin arvo, joka on 25):
avain = "Aapeli"
print(oppilaat[avain])      #sama kuin:  print(oppilaat["Aapeli"])


print()

#Etsitään kaikki sanakirjan arvot for/in -loopin avulla:
for i in oppilaat:
    print(oppilaat[i])          #tässä tulostetaan avaimen avulla sen arvo. #i on vuorotellen sanakirjan avain.

#eli uudelleen: #Kun sanakirja läpikäydään for/in-rakennetta käyttäen,
#saa kierrosmuuttuja arvokseen vuoron perään kunkin sanakirjassa esiintyvän AVAIMEN.


print()

#if / in -rakenteella voidaan myös hakea sanakirjasta tietoa:
nimi = input("Anna nimi, niin etsin sen sanakirjasta, jos löytyy: ")
if nimi in oppilaat:
    print(f"Oppilas {nimi} löytyi ja hänen ikänsä on {oppilaat[nimi]}.")
if nimi not in oppilaat:
    print("Nimeä ei löydy sanakirjasta!")

print()

#lisätään uusi oppilas, mikäli nimeä ei löydy sanakirjasta
#jos avain löytyy, ohjelma muokkaa olemassa olevaa avainta (muokkaa arvon eli iän):
oppilaat["Ulla"] = 22           #tässä lisätään uusi oppilas ja ikä sanakirjaan
print(oppilaat)                 #tulostetaan muokattu sanakirja


#sanakirja[avain] = arvo    #tällä notaatiolla voi lisätä avaimen ja arvon sanakirjaan.


print()
#tyhjän sanakirjan voi luoda kaarisulkeiden {} avulla:
my_dict = {}
print(type(my_dict))        #tulostetaan tyyppi: <class 'dict'>

######################
print()
######################

#mod7: sanakirja: esim. lainausmerkin sisällä tulee käyttää heittomerkkejä! = ' ', muuten ei tunnista avainta
#esim1.
yhteystiedot = {"Viivi" : "050-1234567", "Ahmed" : "040-1112223"}
print(f"Viivin numero on {yhteystiedot['Viivi']}")      #hyödynnetään avainta arvon hakemiseen

#lista.index    hakee listan alkion järjestysnumeron.
# lista = ["a", "b", "c"]
# print(lista.index("a"))

#Sanakirjaan voi tallentaa useampia arvoja yhteen avaimeen: esim. nimi ja arvot: puh.nro, osoite, myös
#..useita avaimia. Eli alla: puh ja osoite ovat yhdessä yksi arvo.

#esim2. MONIULOTTEINEN SANAKIRJA (1. tenttiin ei tule tätä)
yhteystiedot2 = {
    "Viivi" : {"puh" : "050-1234567", "osoite" : "Pikkutie 15"},
    "Ahmed" : {"puh" : "040-1112223", "osoite" : "Katajamutka 42"}
}
print(f"Viivin osoite on {yhteystiedot2['Viivi']['osoite']}")
print(f"Ahmedin osoite on {yhteystiedot2['Ahmed']['osoite']}")

#eli laittamalla avaimen 'Viivi' ja perään toisen avaimen 'osoite' päästään arvoon, jossa lukee osoite.
# sanakirja[avain][avain]   tulostaa siis moniulotteisesta sanakirjasta halutun arvon

#avaimen tulee olla aina uniikki, esim. ei voi olla kahta avainta "Viivi", mutta arvot voivat olla sama,
#.. eli esim. sama puhelinnumero tai sama osoite saa olla
