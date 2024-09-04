# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
# käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

cities = []

for city in range(5):                   #kysytään kaupunki (viisi kertaa)
    city = (input("Kerro kaupunki: "))
    cities.append(city)                 #tallennetaan kaupunki listaan

for city in cities:                     #tulostetaan listasta kaupungit yksi kerrallaan
    print(city)
