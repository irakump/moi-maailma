import requests
import requests.exceptions
import json

api_key = ""        # api-key poistettu

# sääpalvelussa voi vaihtaa myös kielen argumentilla lang:
finnish_metric = "&units=metric&lang=FI"

def get_weather(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}{finnish_metric}"

    # virheiden käsittely
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print("Verkkovirhe!")
        return

    # testataan, että HTTP-statuskoodi on ok, muuten lopetetaan suoritus
    if response.status_code != 200:
        print(f"HTTP-yhteysvirhe {response.status_code}")
        return

    # parsitaan JSON-datasta Pythonin tietorakenne (lista jonka sisällä sanakirjoja ja listoja)
    response_body = response.json()

    if len(response_body) < 1:
        print("Ei tuloksia.")
        return


    #print(json.dumps(response_body, indent=2))     # tämä tulostaa siistimmässä muodossa responsen
    temperature = response_body["main"]["temp"]
    print(f"Lämpötila kaupungissa {city_name} on {temperature} Celsiusastetta.")
    description = response_body["weather"][0]["description"]
    print(f"Sään kuvaus: {description}")

# pääohjelma
city_name = input("Syötä kaupungin nimi: ")
get_weather(city_name)
