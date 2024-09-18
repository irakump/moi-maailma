#Tenttikertaus, mod7
#MONIKKO (tuple), JOUKKO (set) ja SANAKIRJA (dictionary)

#MONIKKO:
#monikko merkitään (), luodaan monikko = ()
#monikkoa ei voi muokata, alkiot ovat aina samassa järjestyksessä. Kätevä esim. viikonpäiville
#muutoin monikko on kuin lista, mutta käytetään kaarisulkeita (listassa hakasulkeet [])

weekdays = ("ma", "ti", "ke", "to", "pe", "la", "su")
user_input = 3               #int(input("Kerro viikonpäivän järjestysnumero (1-7): "))
print(f"{user_input}. viikonpäivä on {weekdays[user_input -1]}.")

print(weekdays)

#monikon sisältämät arvot voidaan purkaa muuttujiin:
fruits = ("banaani", "sitruuna", "päärynä")
(first, second, third) = fruits
print(f"Hedelmiä ovat {first}, {second} ja {third}.")

#JOUKKO:
#joukko merkitään {}, tyhjä joukko luodaan: joukko = set(), alustettu: joukko = {1, 2, 3, 4}
#joukossa alkiot eivät ole järjestyksessä, eli ei voi viitata tiettyyn alkioon indeksillä.
# (joukko on siis järjestämätön)
#joukossa yksi arvo voi esiintyä vain yhden kerran, muissa voi esiintyä sama useammin

#######
print()
#######

#esim.
games = {"Monopoly", "Shakki", "Mario Kart"}
print(games)
games.add("Kimble")                 #add-komennolla voi lisätä alkion joukkoon
print(games)
games.add("Monopoly")               #alkio on jo listassa, joten ei tapahdu mitään.
print(games)
games.remove("Shakki")              #remove-komennolla voi poistaa alkion joukosta
print(games)

for g in games:                     #tulostaa joukon alkiot yksitellen, satunnaisessa järjestyksessä
    print(g)

#tyhjän joukon luominen:
nimet = set()                   #tulee käyttää set() -komentoa, sillä aaltosulkeet luovat sanakirjan!
nimet.add("Lisa")
nimet.add("Bart")
print(nimet)

########
print()
########

#SANAKIRJA:
#sanakirja merkitään {}, luodaan sanakirja = {}
#sanakirjassa voi luoda avain-arvopareja
ages = {"Gerbert" : 6, "Herbert" : 40, "Gabrielle" : 8, "Fiona" : 101}
print(ages)     #tulostuu sanakirja sellaisenaan, avain-arvoparit näkyy
print(ages["Herbert"])    #tulostuu Herbert-avaimen kautta ikä (40)
print(ages["Fiona"])              #101

name = input("Anna nimi: ")
if name in ages:                #jos nimi on sanakirjassa, haetaan sitä vastaava arvo
    print(f"Henkilön {name} ikä on {ages[name]}.")
else:
    print("Nimeä ei löytynyt.")

#arvon lisääminen sanakirjaan:
ages["Gilderoy"] = 47           #eli: sanakirjan_nimi[avain] = arvo         #avain hakasulkeisiin
print(ages)
ages["Minerva"] = 71
print(ages)

for a in ages:
    print(a)            #tulostuu vuorotellen jokainen AVAIN (tässä tapauksessa nimi)
    