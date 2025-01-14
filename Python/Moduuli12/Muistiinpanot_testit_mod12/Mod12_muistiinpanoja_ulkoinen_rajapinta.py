# Moduuli 12 - ULKOISEN RAJAPINNAN KÄYTTÖ (lyhenne: API = application programming i...)

# Asiakas-palvelin -malli: se laite, joka ottaa yhteyden palvelinkoneeseen (ja siinä olevaan palvelinlaitteeseen),
# lähettää aluksi pyynnön (request). Palvelin käsittelee pyynnön ja tuottaa vastauksen (response).

    # asiakas ---HTTP-pyyntö--> palvelin
    # asiakas <--HTTP-vastaus-- palvelin

# ohjelmointirajapinnan kautta voi käyttää esim. sääpalveluita, avoimia tietokantapalveluita (internetin julkisilta
# palveluntarjoajilta)

# voisi tehdä esim. ohjelman, joka hakee HSL:n rajapinnasta tietyn pysäkin seuraavat tulevat bussit ja kellonajat
    # --> muodostuu applikaatio

# Pyynnön lähettäminen: HTTP:llä on viisi (yleisesti käytettyä) operaatiota:

    # GET = lukee sisältökohteen // käytetään tavallisiin verkkosivujen hakupyyntöihin
    # PUT = korvaa olemassa olevan sisältökohteen
    # POST = luo uuden sisältökohteen // esim. kirjautumislomakkeen täyttäminen verkkosivuilla
    # PATCH = muokkaa olemassa olevaa sisältökohdetta
    # DELETE = poistaa olemassa olevan sisältökohteen

# statuskoodit:
    # 200-alkuiset: kaikki ok
    # 300-alkuiset: ok, mutta matkan varrella "jotakin muuttuu"
    # 400-alkuiset: virhe asiakaspäässä
    # 500-alkuiset: pyyntö ok (asiakaspäässä), mutta palvelimella joku pielessä

# esim1. - get-pyyntö rajapintaan (GET https://api.tvmaze.com/search/shows?q=emmerdale)

import requests
import requests.exceptions


def search_show(search_term):

    # haetaan tieto rajapinnasta, tallennetaan muuttujaan
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"

    # Käsitellään mahdolliset virheet verkkoyhteydessä
    # --> jos sovellus yrittää kaatua, estetään se ja koodin suoritus siirtyy
    try:
        response = requests.get(url)    # jos tässä tulee virhe, suoritetaan except ja vältetään virhe
    except requests.exceptions.RequestException as e:   # luodaan virhe-olio nimeltä e
        print("Verkkovirhe.")
        #print(e)               # nämä tiedot kiinnostavat vain kehittäjiä, ei tarvitse näyttää käyttäjälle
        return

    # testataan, että http-statuskoodi on ok (jos ei ole, niin lopetetaan funktion suoritus)
    #print(response.status_code)
    if response.status_code != 200:
        print(f"HTTP-yhteysvirhe {response.status_code}")
        return

    response_body = response.json()      # JSON on JavaScriptin ominaisuus - data muutetaan pythonin tietorakenteeksi

    if len(response_body) < 1:
        print("Ei tuloksia.")
        return                          # tämä lopettaa funktion toiminnan

    # käydään HTTP-vastauksen runko (response_body) läpi for-silmukalla (toistorakenteella)
    print("-------------------\nKaikki hakutulokset:\n-------------------")
    for item in response_body:                                  # item = asia
        print(f"Nimi: {item['show']['name']}")                  # tässä käytetään kahta avainta: show ja name, ja tulostuu sarjan nimi
        print(f"TV-ohjelman tyyppi: {item['show']['type']}")

        for genre in item['show']['genres']:
            print(f"Genre: {genre}")
        print("-------------------")

search_show(input("Anna TV-hakusana: "))

# TRY: virheen käsittelyyn
# try:
#   something
# except:       # eli jos "something"-kohdassa tulee virhe, ohjelma siirtyy eteenpäin eikä kaadu
#   print("virhe")
#   return

