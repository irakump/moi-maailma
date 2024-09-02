# Vko 3 / mod5: Listarakenne ja for-toistorakenne. Funktio.

"""
LISTARAKENNE []
-Listaan liitettävät jäsenet luetellaan hakasulkeiden sisällä pilkulla erotettuina
-listan rakenne: alkaa nrosta 0 (0. alkio)
"""
from codecs import xmlcharrefreplace_errors

#esim1. - ilman listaa
name1 = "Hagrid"
name2 = "Alruuna"
name3 = "Mörkö"
age1 = 13
age2 = 5
age3 = 130

#kaikista muuttujista tulee tehdä oma tuloste
print(f"Hei {name1}, ikäsi on {age1} vuotta.")
print(f"Hei {name2}, ikäsi on {age2} vuotta.")
print(f"Hei {name3}, ikäsi on {age3} vuotta.")

print("-------------------------------")

#esim2. - sama listalla: luodaan listat ja lisätään muuttujat listaan
names = ["Hagrid", "Alruuna", "Mörkö", "Harry", "Petteri", "Bellatrix"]      #tai [name1, name2, name3, ...]
print(names)    #koko lista tulostuu

#names2 = [name1, name2, name3]
#print(names2)
#print("-------------------------------")

ages = [age1, age2, age3, 1, 89, 38]
print(ages)
print("-------------------------------")

#viittaukset listan alkioihin (alkaa nollasta, eli ensimmäinen alkio on 0, toinen 1)

#listan pituus voidaan tarkistaa len() -funktiolla (lenght)
lenght_names = len(names)
lenght_ages = len(ages)
print(f"Nimi-listan pituus on {lenght_names}.")
print(f"Ikä-listan pituus on {lenght_ages}.")

print("-------------------------------")
#alkioon viitataan indeksinumerolla:

# print(names[3], ages[3])
print(f"Hei {names[3]}, ikäsi on {ages[3]}.")

#listan sisälle voi tehdä listoja
#nimet ja iät voisi lisätä samaan listaan

#viittaus listan ulkopuolelle tuottaa virheen - esim. listassa on 5 alkiota ja viitataan alkioon nro 7
#esim. print(names[9])

print("-------------------------------")

#listan läpikäynti while-silmukan avulla:
iterator = 0                                #iteraattori on kierrosmuuttuja
while iterator < len(ages):                 #loop pyörii niin kauan, kun koko lista on käyty läpi
    print(f"Hei {names[iterator]}, ikäsi on {ages[iterator]}.")
    iterator = iterator + 1     #sama kuin iterator += 1

print("-------------------------------")
#yllä: iterator < len(ages) --> ei voi olla <=, koska alkiot alkavat nollasta!

#listaviittaukset:
names2 = ["Hagrid", "Alruuna", "Mörkö", "Harry", "Petteri", "Bellatrix"]

print(names2[1:3])       #alkaen alkiosta 1, päättyen alkioon 3. Tulee mukaan 1, 2 alkiot, mutta ei 3.
#eli päättyvää alkiota ei oteta mukaan tulostukseen. Jos haluaa tulostaa alkiot 1-3, tulee olla:
print(names2[1:4])   #alkiot 1, 2, 3
print(names2[3:])    #kaikki loput alkiot alkaen 3
print(names2[-1])    #listan viimeinen alkio #-2 on toiseksi viimeinen
#jos tulostaa useamman alkion, tulostus on listamuotoinen
#jos tulostaa vain yhden alkion, tulostuu pelkkä nimi

print(names2[2:5:2])        #indeksistä 2 indeksiin 5, joka toinen tulostuu

print("-------------------------------")

#listaan voi yhdistää erilaisia tietorakenteita (esim. nimet ja iät samaan)
lista1 = ["Ulla", "Matti", "Ilkka"]
yhdistetty_lista = [23, 45, 66, 67, 68, lista1]       #listan sisällä toinen lista
print(yhdistetty_lista)
print(yhdistetty_lista[5])      #lista1 on viides alkio
print(yhdistetty_lista[5][0])   #listan sisäisestä listasta halutaan tulostaa Ulla, hakee lista1:sta ensim. alk.

print("-------------------------------")

#LISTAOPERAATIOT    (alkioiden lisäys, poisto)
#esim.
"""
nimet = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while nimi!="":
    nimet.append(nimi)
    nimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

print(nimet)
"""

print("-------------------------------")

#python-listoja voi katsoa: w3schools.com - python-lists

#uuden alkion lisäys listan loppuun:  LISTAN_NIMI.append()
names = ["Hagrid", "Alruuna", "Mörkö", "Harry", "Petteri", "Bellatrix"]
names.append("Voldemort")
print(names)

print("-------------------------------")

#alkion poistaminen (ensimmäisen nimen ilmentymän poisto, eli jos nimi on kahdesti, ensimmäinen nimi poistuu)
#names.remove("Petteri")     #jos nimeä ei löydy, tulee virhe

if ("Petteri" in names):        #voi kokeilla, löytyykö nimi listasta (tämän voi tehdä ennen poistoa)
    print("Petteri löytyi listasta! Poistetaan se.")
    names.remove("Petteri")
    print(names)

#esim. - lisää alkio haluttuun kohtaan: insert - lisätään Petteri takaisin, mutta listan ensimmäiseksi (alkio 0)
names.insert(0, "Petteri")
print(names)

#kokeillaan, monentenako lisätty nimi (Petteri) on: INDEX
#index kertoo alkion ensimmäisen sijainnin indeksin
print(names.index("Petteri"))

print("-------------------------------")

#lisätään uusia nimiä listaan:  EXTEND     #lisää pelkät nimet, ei koko listaa alkuperäisen listan sisään
more_names = ["Dumbledore", "Hermione", "Dobby"]
names.extend(more_names)
print(names)

#listojen yhdistäminen (toinen tapa)
lista1 = ["aa", "hoo", "cee"]
lista2 = ["yy", "gee", "bee"]
new_lista = lista1 + lista2
print(new_lista)

#muokataan olemassa olevaa alkiota:
names[6] = "Lordi Voldemort"            #muokkaa indeksin 6 nimeä "Voldemort"
print(names)

#jos haluaa muokata useaa alkiota, voi ne laittaa silmukkaan (while)

#SORT: lajittelu aakkos- tai suuruusjärjestykseen
new_lista.sort()
print(new_lista)

print("-------------------------------")

num_lista = [6, 3, 4, 1, 0, 8]
num_lista.sort()        #sulkuihin voi laittaa tavan esim. reverse = väärinpäin. jos ei mitään = aakkosjärj.
print(num_lista)        #pitää ensin sortata, ja sitten tulostaa

