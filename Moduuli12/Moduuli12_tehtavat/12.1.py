import requests
import requests.exceptions
import json

# Tehtävä 12.1
# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle. Käytä seuravalla sivulla
# esiteltävää rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.

def get_chuck_norris_joke():

    url = "https://api.chucknorris.io/jokes/random"
    #print(url)

    # virheiden käsittely
    try:
        response = requests.get(url)#.json()
    except requests.exceptions.RequestException:
        print("Verkkovirhe.")
        return

    if response.status_code != 200:
        print(f"HTTP-yhteysvirhe {response.status_code}.")
        return

    print(response)
    print(json.dumps(response, ident=2))

get_chuck_norris_joke()


