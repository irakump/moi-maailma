# Tehtävä 7.3
# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot
# vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman
# ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan
# lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta
# kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
# Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

#alustetaan sanakirja, jossa avain on ICAO-koodi ja arvo on lentokentän nimi
airport_dictionary = {"EFHK": "Helsinki-Vantaa Airport",
                      "EFTP" : "Tampere-Pirkkala Airport", "EFRO" : "Rovaniemi Airport"}

#kysytään käyttäjältä toiminto ensimmäisen kerran
user_input = input("Valitse seuraavista (A, B tai C):"
                   "\nA: syötä uusi lentoasema\nB: hae syötetyn lentoaseman tiedot\nC: lopeta\n")

while (user_input != "C"):
    if (user_input == "A"):                                 #A: käyttäjä syöttää uuden lentoaseman
        icao_code = input("Syötä lentoaseman ICAO-koodi: ")
        airport_name = input("Syötä lentoaseman nimi: ")
        airport_dictionary[icao_code] = airport_name        #lisätään ICAO-koodi ja lentokenttä sanakirjaan
    elif (user_input == "B"):                               #B: haetaan syötetyn lentoaseman tiedot
        icao_code = input("Syötä lentoaseman ICAO-koodi: ")
        print(f"Lentoaseman nimi on {airport_dictionary[icao_code]}.")    #tulostetaan arvo (lentoaseman nimi)

    #kysytään käyttäjältä toiminto uudelleen
    user_input = input("Valitse seuraavista (A, B tai C):"
                       "\nA: syötä uusi lentoasema\nB: hae syötetyn lentoaseman tiedot\nC: lopeta\n")

print("Ohjelma lopetettu.")            #kun käyttäjä syöttää "C", ohjelma päättyy, ilmoitetaan siitä tulosteella.
