#Muuttujilla ja vakioilla voi tehdä laskutoimituksia
# + yhteenlasku, - vähennyslasku, * kertolasku, / jakolasku
# % jakojäännösoperaatio, // jakolasku, joka palauttaa pelkän kokonaisluvun
# ** potenssiinkorotus

#merkkijonon muuttaminen liukuluvuksi: float
#merkkijonon muuttaminen kokonaisluvuksi: int
#luku muunnetaan merkkijonoksi: str - jos on luku ja merkkijono samassa, lukee luku muuttaa.

#fahrenheit_str = input("Anna lämpötila Fahrenheit-asteina: ")
#fahrenheit = float(fahrenheit_str)
#celsius = (fahrenheit-32)*5/9
#print("Lämpötila celsius-asteina: " + str(celsius))

#input-funkioon laitettava arvo tulkitaan aina merkkijonoksi, siksi tulee vaihtaa numeroksi
#kuten yllä: float (liukuluku) tai int (kokonaisluku).

#MUOTOILUMERKKIJONOLITERAALIT: ns. muotoilukoodit:
#rajataan, montako merkkiä on tilaa merkkijonolle tai montako desimaalia näkyy

#edellä oleva uudelleen, mutta rajatummin:
fahrenheit_str = input("Anna lämpötila Fahrenheit-asteina: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit-32)*5/9
print(f"Lämpötila celsius-asteina: {celsius:6.2f}")
#f-kirjain kertoo, että tulostettava merkkijono sisältää muotoiltavia lausekkeita
#ilman edessä olevaa f-kirjainta tulostus sisältäisi myös {}-merkit
# {} = aaltosulkeet
#muotoiltava lauseke kirjoitetaan aaltosulkeiden sisään, yllä se on liukuluku celsius
# merkintä 6.2 tarkoittaa, että tulos esitetään 6 merkkiä leveässä kentässä, ja esitys-
#tarkkuus on 2 desimaalia.

#esimerkkejä muotoilukoodeista: .5f (liukuluku 5 desimaalin tarkkuudella)
# 10.2f (liukuluku 2 desim. tarkkuudella 10 merkkiä leveään kenttään)
# <20s (merkkijono 20 merkkiä leveään kenttään vasemman reunan mukaan tasattuna
# 8d (kokonaisluku 8 merkkiä leveään kenttään)

#KIRJASTOJEN AVAAMINEN: import (esim. matikka: import math, aina tiedoston alkuun)
#import = tuontilause

