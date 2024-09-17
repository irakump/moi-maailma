#Tenttikertaus, moduuli 6
#FUNKTIO

#toistuvat ohjelman osat kannattaa koodata funktioksi - toistoa kannattaa välttää
#funktiot ovat aliohjelmia, joita kutsutaan toisesta ohjelmasta (pääohjelmasta)
#on olemassa myös toinen aliohjelma (metodi), josta lisää olo-ohjelmoinnissa (mod9)

#Funktion rakenne:
#FUNKTIO
#PÄÄOHJELMA, joka kutsuu funktiota, sijaitsee siis funktion ulkopuolella
#funktio tulee määritellä ennen pääohjelmaa, jotta sitä voi käyttää.

#funktiot voivat kutsua toisia funktioita, eli samassa ohjelmassa voi olla useita eri funktioita
#kutsuminen tarkoittaa sitä, että pääohjelman suoritus siirtyy funktioon.

#esimerkki:
def tervehdi():
    print("Hei!")
    return

#funktio määritellään def-sanan avulla. Sitä seuraa funktion nimi, joka on verbi - nyt nimeltään tervehdi.
#aina pitää olla myös sulkeet () ja kaksoispiste :
#jos funktion nimessä on useampi sana, ne yhdistetään alaviivalla, esim. tervehdi_kayttajaa
#kaarisulkeiden sisälle määritellään parametrit, joita voi olla useita. Jos ei laita mitään, pitää olla ()

#pääohjelma:
print("Päivä alkaa tervehdyksellä.")
tervehdi()                              #tässä tulostuu funktion printti eli Hei!

#FUNKTION PARAMETRIT:
#funktiolle tulee joskus väittää jotakin tietoja = parametreja, samaa funktiota voi käyttää eri tavoin
#parametreja ei tarvitse, jos funktion kuuluu toimia aina samalla tavalla, kuten yllä.
#parametrien arvot välitetään funktion kutsussa

#esim2.
def tervehdi(kerrat):       #kerrat on pelkkä nimi, ja kertoo, mitä tietoa tulee pääohjelmasta antaa
    for i in range(kerrat):
        print(f"Hei {i+1}. kerran!")      #jos on pelkkä i, ensimmäisen kerran tulostuu "..0. kerran!")
    return

#pääohjelma
print("Päivä alkaa tervehdyksillä.")
tervehdi(5)                                 #parametrin arvoksi asetetaan 5

#funktiolle välitettäviä parametrien arvoja kutsutaan ARGUMENTEIKSI.

#Paikallinen muuttuja (funktion sisäinen) vs. globaali muuttuja (ulkoinen muuttuja):

#funktion sisällä olevat muuttujat ovat PAIKALLISIA MUUTTUJIA (eivät näy funktion ulkopuolelle,
#..eli niitä ei voi käyttää muualla kuin funktion sisällä (esim. yllä kierrosmuuttuja i)
#funktion ulkopuolella määritetty muuttuja = GLOBAALI MUUTTUJA, sitä voi käyttää sekä funktion ulko-
#puolella että sisällä, ja sitä voi muokata myös funktion sisällä. Jos muokataan funktion sisällä,
#se tulkitaan paikalliseksi muuttujaksi, eli globaalin muuttujan arvo ei muutu.

#esim.
def vaihda():
    kaupunki = "Vantaa"                         #luodaan sisäinen muuttuja
    print(f"Kaupunki lopuksi: {kaupunki}")

#pääohjelma
kaupunki = "Helsinki"                           #luodaan globaali muuttuja
print(f"Kaupunki aluksi: {kaupunki}")           #tässä kaupunki on Helsinki
vaihda()                                        #tässä kaupunki muuttuu: Vantaa, ja tulostuu
print(f"Kaupunki lopuksi: {kaupunki}")          #tässä kaupunki on edelleen Helsinki.

#eli: funktion sisäisen muuttujan vaihtaminen EI MUUTA globaalin muuttujan arvoa.

#PARAMETRIT (useita parametreja):
#funktiolle voidaan välittää useita argumentteja (erotetaan toisistaan pilkulla)
#argumenttien arvot sijoitetaan parametrimuuttujiin siinä järjestyksessä kuin ne esiintyvät.

def tervehdi(tervehdys, kerrat):
    for i in range(kerrat):
        print(f"{tervehdys} {i+1}. kerran!")
    return

#pääohjelma:
tervehdi("Moi", 4)
tervehdi("Hyvää päivää", 2)

#yllä: samaa muuttujaa voi käyttää siis useaan erilaiseen tulostukseen, kun asettaa parametreja.

#FUNKTION PALUUARVO:
#funktion tuottama arvo palautetaan return-lauseella
def summaa(eka, toka):
    sum = eka + toka
    return sum                  #tässä paluuarvona on summa

number1 = float(input("Anna ensimmäinen luku: "))
number2 = float(input("Anna toinen luku: "))
result = summaa(number1, number2)                               #tässä paluuarvo tallennetaan muuttujaan
print(f"Lukujen {number1} ja {number2} summa on {result}.")

print(f"Lukujen {number1:.3f} ja {number2:.3f} summa on {result:.3f}.")

########
print()
########

#LISTA voi olla parametrina:

def luettele(nimi):
    print("Luokassa on seuraavat oppilaat:")
    for i in nimi:
        print(f"-{i}")
    return

#pääohjelma
students = ["Hermione", "Ron", "Malfoy", "Goyle", "Pansy", "Neville"]
luettele(students)
print(f"Yksi oppilas erotetaan: {students[2]}.")
students.remove(students[2])
luettele(students)
new_name = input("Luokkaan saapuu uusi oppilas. Kerro nimi: ")
students.append(new_name)
luettele(students)

#clear-komenolla voi tyhjentää listan.

print(f"Lukuvuosi päättyy. Yksi oppilas jäi luokalle: {students[3]}.")
name = students[3]          #tallennetaan muuttujaan
students.clear()            #listan tyhjennys
students.append(name)       #lisätään tallennettu nimi listaan
luettele(students)          #tulostuu alkuperäisen listan 3. alkio eli Pansy.

