#Tenttikertaus, 1. Python tentti

#MODUULI 2: muuttujat ja muuttujien perustyypit, luvut, laskutoimitukset

# muuttuja = variable, tallennetaan käyttäjän syöte muuttujaan

print("Moi maailma")
#######
print()
#######

#rivinvaihtomerkki \n

print("Moi")
print("avaruus")
#sama uudelleen:
print("Moi taas\navaruus")


#########
print()
#########

#muuttuja name, kysytään käyttäjältä syöte inputin avulla
name = input("Kerro nimesi: ")      #kysytään syöte ja samalla tallennetaan se muuttujaan
print("Hei, " + name + "!")
#tai f-stringin avulla:
print(f"Hei taas, {name}!")     #muuttuja merkitään hakasulkeisiin lainausmerkkien sisään

#########
print()
#########

#Python-kielessä on kuusi muuttujan perustyyppiä:

# 1. merkkijono (string) - lainausmerkeissä: "tämä kaikki on merkkijonoa"
# 2. luku (number) - joko int (kokonaisluku, esim. 4) tai float (liukuluku, esim. 4.56)
# voi olla myös pitkä kokonaisluku (esim. 1234579000) tai kompleksiluku (esim. 3-2i)
# 3. totuusarvo (boolean) - True tai False
# 4. lista (list), merkitään hakasulkeilla []
# 5. monikko (tuple), merkitään kaarisulkeilla (), muuttumaton
# 6. sanakirja (dictionary), merkitään hakasulkeilla {}

#lisäksi on olemassa joukko (set), merkitään kaarisulkeilla {}, mutta luodaan: set()
# my_dictionary = {} luo sanakirjan, siksi joukkoa luodessa tulee käyttää set-komentoa

#luvun desimaali merkitään aina pisteellä . !

print(4 + 1.2)  #laskee ja tulostaa summan
print(f"Lukujen 4 ja 1.2 summa on {4 + 1.2}.")

#########
print()
#########

#Laskutoimitukset ja tyypinmuunnosfunktiot:
#yhteenlasku +, vähennyslasku -, kertolasku *, jakolasku /
#jakojäännösoperaatio %     #palauttaa jakojäännöksen, esim. 6 % 2  --> tuloste: 2
print(6%4)      #tulostaa 2, koska jakojäännös on 1,5 niin pyöristää ylöspäin?
# pelkän kokonaisosan palauttava jakolasku //   #esim. 7//2 palauttaa 3
print(7//2)
# potenssiinkorotus **

#########
print()
#########

#esim.
#lämpötila celsius-asteina:
celsius = 24.1234567
print(f"Lämpötila Celsius-asteina: {celsius:6.2f}") #tässä annetaan 6 merkkiä tilaa luvulle, 2 desim. tarkkuudella

#ilman muotoilukoodia:
print(f"Lämpötila Celsius-asteina: {celsius}")

#######
print()
#######

import math     #saa matikkakirjaston
print(f"Piin likiarvo 5 desimaalin tarkkuudella on {math.pi:.5f}")

