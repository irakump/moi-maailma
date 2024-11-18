# Tehtävä 12.1
# Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle. Käytä seuravalla sivulla
# esiteltävää rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests
import json

url = "https://api.chucknorris.io/jokes/random"

# value = avain

try:
    request = requests.get(url)
    if request.status_code == 200:
        json_response = request.json()
        #print(json.dumps(json_response, indent=2))
        print(json_response["value"])
except requests.exceptions.RequestException as e:
    print("HTTP-yhteysvirhe")
