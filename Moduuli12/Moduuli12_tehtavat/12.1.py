# Tehtävä 12.1
# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle. Käytä seuravalla sivulla
# esiteltävää rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests
import requests.exceptions

def get_chuck_norris_joke():

    url = "https://api.chucknorris.io/jokes/random"

    # virheiden käsittely
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print("Verkkovirhe.")
        return

    if response.status_code != 200:
        print(f"HTTP-yhteysvirhe {response.status_code}.")
        return

    response_body = response.json()         # muutetaan data pythonin tietorakenteeksi
    print(response_body["value"])           # tulostetaan vitsi

get_chuck_norris_joke()
