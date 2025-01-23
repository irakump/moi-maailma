# MODUULI 12 - ULKOISEN RAJAPINNAN KÄYTTÖ

# termit: ULKOINEN RAJAPINTA (API), PALVELIN, PYYNTÖ = REQUEST, VASTAUS = RESPONSE

# tiedon siirto Internetissä: asiakas-palvelin-malli

# PALVELIN = verkkoon kytketty tietokone, joka odottaa siihen kohdistuvia yhteydenottoja
            # eli tietokoja joka toimii palvelinlaitteena TAI palvelinlaitteeseen asennettu palvelinohjelmisto

# ensin laite (asiakas) ottaa yhteyden palvelinkoneeseen ja lähettää pyynnön = REQUEST
# sitten palvelin käsittelee pyynnön ja tuottaa vastauksen = RESPONSE

# RAJAPINTA = internetin julkiset palveluntarjoajat antavat mahdollisuuden käyttää niitä ohjelmallisesti, eli rajapinnasta voi hakea tietoa

# HTTP-pyyntöjen viisi yleisesti käytettyä operaatiota:
# GET = lukee sisältökohteen        # tämä yleisin, käytetään verkkosivujen hakupyyntöihin
# PUT = korvaa olemassa olevan sisältökohteen
# POST = luo uuden sisältökohteen
# PATCH = muokkaa olemassa olevaa sisältökohdetta
# DELETE = poistaa olemassa olevan sisältökohteen

# REST-suunnitteluperiaatteet = rajapinta suunnittelussä hyödynnetään kaikkia viittä (yllä olevaa) operaatiota (on muitakin
    # suunnitteluperiaatteita (ei nyt käsitellä) )

# get-pyyntö python-ohjelmassa:
# pitää importata requests-paketti:
import requests
import json

hakusana = input("Anna hakusana: ")
url = f"https://api.tvmaze.com/search/shows?q={hakusana}"
vastaus = requests.get(url).json()
#print(vastaus)

# yllä oleva palauttaa vastauksen JSON-muodossa, eli lista, joka sisältää sanakirjoja

# vastauksen käsittely
# funktio json.dumps() muotoilee vastauksen paremmaksi, siistimmäksi:
#print(json.dumps(vastaus, indent=2))     # pitää laittaa alkuun: import json

# jos halutaan hakea elokuvan nimi, tulee käyttää indeksejä ja avaimia:
# print(vastaus[0]["show"]["name"])       # pitää olla lainausmerkit, koska ei ole määritelty show-muuttujaa

# halutaan tulostaa jokainen löytynyt ohjelman nimi --> toistorakenne
for v in vastaus:
    print(v["show"]["name"])        # v:n arvoksi tulee vuorotellen indeksi 0:sta alkaen, kunnes vastaus on käsitelty

# virheenkäsittely - 2 seikkaa: vastauksen mukana tuleva HTTP-statuskoodi sekä Python-ohjelmassa syntyvät poikkeukset
# HTTP-statuskoodi 200: pyyntöön vastataan onnistuneesti
# 400: virhe

# vastauksen mukana tuleva statuskoodi voidaan lukea ohjelmallisesti requests.get-metodin ominaisuudesta status_code
# se testaa, onko statuskoodi 200 vai joku muu (suppea)

# AJONAIKAINEN POIKKEUS = ulkoiseen palveluun ei saada lainkaan yhteyttä eikä palvelu pääse palauttamaan virheestä kertovaa
# statuskoodia. Python-ohjelma siis kaatuu ajonaikaiseen virhetilanteeseen.
# poikkeuksen käsittely toteutetaan try/except -rakenteella

# jokainen python-poikkeus on olio
# repuests-kirjaston tuottamat poikkeukset ovat RequestException -luokasta periytyvien luokkien ilmentymiä

###
print()
###

# virhetarkistuksilla täydennetty ohjelma:
import json
import requests

hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyynto = "https://api.tvmaze.com/search/shows?q=" + hakusana

try:
    vastaus = requests.get(pyynto)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(json.dumps(json_vastaus, indent=2))
        for a in json_vastaus:
            print(a["show"]["name"])
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")


