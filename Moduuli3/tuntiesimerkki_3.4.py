# Tehtävä 3.4: tunnilla näytetty esimerkki, lyhyempi tapa kuin oma

year = int(input("Kerro vuosiluku: "))

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")

#bonus: ohjelma tulostaa kaikki karkausvuodet annettuun vuosilukuun asti

iterator = 0                #aloitetaan vuodesta 0      #iteraattori on toistorakenteeseen liittyvä toiminnallisuus
while iterator < year:      #loop pyörii niin kauan, kun luku on pienempi kuin annettu vuosiluku
    iterator += 4           #lisätään edelliseen lukuun 4 (sama kuin iterator = iterator + 4)
    if (iterator % 400 == 0) or (iterator % 100 != 0):
        print(f"{iterator} on karkausvuosi.")
