# kommentteja voi merkitä hashtag-merkillä pythonissa
# tallenna ctrl + s

#mod02: tulosteet voi kirjoittaa eri riveille tekemällä kaksi print-komentoa:
# print("moi")
# print("ihminen")

# TAI rivinvaihtomerkillä \n eli sama tuloste tulee seuraavalla:
# print("moi\nihminen)"
#testi:
# print("moi\nihminen")
# print("moi")
# print("ihminen")

# käyttäjä = input("Anna nimesi: ")
# print("Hauska tavata, " + käyttäjä + "!")

#ohjelmoidessa ei pidä käyttää erikoismerkkejä: ääkköset, huutomerkit yms, välilyönti.
#nimissä voi käyttää kuitenkin viivaa tai alaviivaa.
#aina kun luo uuden tiedoston, kannattaa se lisätä (add) gitiin. Eli kansiota luodessa
#..ohjelma kysyy, lisätäänkö gitiin, niin valitse add.
#jos nimen vaihtaa, voi valita "search for references", jolloin se muuttaa nimen muihin..
#..kansioihin, jos niissä on viittauksia toisiinsa.

#input=syöte, käyttäjältä ohjelmalle
#output= tietoa ohjelmalta käyttäjälle, esim. pelissä pelaaja liikkuu, näyttö päivittyy

#tunneilla käydään läpi tulevia tehtäviä, ohjelmointia ei tarvitse tehdä ns. itsenäisesti
#omaan tahtiin, vaan tunnilla aina esitellään asiat, ja sen jälkeen voi tehdä tehtäviä

# name = "Matti" #tässä on kyseessä muuttujan luominen, ja seuraavassa printataan muuttuja
# print(name)
# muuttuja = "koira"
# print(muuttuja)
# print("Moi " + (name)) #tässä tulosteena on "Moi Matti", laita välilyönti lainausten sisään

#käyttäjän syötteen lukeminen, eli kone kysyy käyttäjältä tietoja, myös muuttuja:
#name = input("Kerro nimesi: ") #sulkuihin kysymys, johon halutaan vastaus
#print("Moi " + name + "!")

#lainausmerkit: jos haluaa tulosteeseen sisältyvän lainausmerkit, tulee käyttää kahta
#eri merkkiä, esim. print('"Hei", sanoi Ville')
#print('"Hei", sanoi Ville')

#pidä koodeissa tyyli yhtenäisenä: käytä aina joko " tai ' merkkiä, ei sekaisin.
# + -merkillä voi liittää termejä toisiinsa
# \ -merkki tarkoittaa, että sen jälkeen tulee joku ctrl-komento??
# \n tarkoittaa rivinvaihtoa. esim. print("Moi \n " + name)
#name = input("Kerro nimesi: ")
#print("Moi \n" + name)

#iän kysyminen:
#age = 7 #tässä tulee muuttuja age
#print(age)
#numeroihin tulee lisätä str ??
#numerosta voi tehdä myös merkkijonon: esim. age = "7", lainausmerkeissä oleva on merkkijono
# merkkijono = string

#age = "7" #merkkijono, jos haluaa lisätä numeron merkkijonoon, voi tehdä näin.
#print("Ikäsi on: " + age)
#jos haluaa laskea numeroilla, älä tee nroa merkkijonoksi,
#esim. ei toimi: age = 7 + "1", muuttujia ei voi sekoittaa.

ika = input("Kerro ikäsi: ")
print("Ikäsi on " + ika)

# --> opettele, miten tehdään "ikäsi on vuoden päästä...", pitää tehdä numerot.

#age2 = 7 + 1 #näin voi laskea, mutta ei lisätä teksitä.
#age2 = str(age2) #tässä muutetaan tulos merkkijonoksi ja tallennetaan edellinen tulos.
#print("Ikäsi on vuoden päästä " + age2)
#jos haluaa lisätä tekstiä, tulee lisätä str
#str(5) #tästä tulee merkkijono: "5"
#str(age2) #tässä muutetaan int (kokonaisluku) merkkijonoksi eli string.

#ks. ohjelmoinnin dokumenteista opettajan esimerkkikoodaukset, ei tarvitse kaikke kirjoittaa
#..itse.

#merkkijonon (str) voi vaihtaa kokonaisluvuksi
#esim. age = "7"
# age = int(age)

#käyttäjän pituus metreinä, liukuluku (float):
height = 1.6 # numeroissa tulee käyttää pistettä, ei pilkkua! piste on desimaalierotin.
#pilkulla on merkitys: erotetaan asioita toisistaan, esim. 1,8,7 on kolme eri nroa
print("Pituus: " + str(height))

#jos haluaa käyttää tarkkoja arvoja (ei pyöristystä), tulee käyttää kokonaislukuja (int).
#float tarkoittaa liukulukua, eli on pyöristetty. Tämä ei käy esim. pankkiasioissa.

#samaan lauseeseen:
# print(f"Nimi: {name}, Ikä: {age}, Pituus: {height}.") #eli muuttujat voi tulostaa {}
#-merkeillä ilman että tarvitsee tehdä tyyppimuutoksia. Ohjelma tunnistaa merkkien kautta.

#eli float on liukuluku, jossa desimaali (piste!) ja int kokonaisluku.
#ohjeissa on tarkemmin, miten voi esittää desimaalin esim. kahden luvun tarkkuudella

#import on avainsana, voi lisätä toiminnallisuuksia/kirjastoja, esim trig. funktiot.
import math # laita importit aina tiedoston alkuun (siisteyden vuoksi)
print(math.pi)  #pii matikkakirjastosta

#tehtävänannon voi kirjoittaa tiedoston alkuun kommenttina, niin tietää mitä tehtävässä tehdään.

# togle comment tai togle line comment - etsi netistä, voi kirjoittaa useita rivejä..
#muistiinpanoja, ilman että tarvitsee jokaista merkata
