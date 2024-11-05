# Tehtävä 12.2
# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma, joka kysyy käyttäjältä
# paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. Perehdy rajapinnan
# dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan
# API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import requests
import requests.exceptions

api_key = ""         # API-avain poistettu tästä

# virheiden käsittely
def test_errors(url):
    try:
        response = requests.get(url)
        return response
    except requests.exceptions.RequestException:
        print("Verkkovirhe.")
        return

    if response.status_code != 200:
        print(f"HTTP-yhteysvirhe {response.status_code}.")
        return

# haetaan koordinaatit
def get_coordinates(city_name, limit=5):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={api_key}"

    response = test_errors(url)
    response_body = response.json()

    lat = (response_body[0]["lat"])
    lon = (response_body[0]["lon"])
    return lat, lon

# haetaan sään nimi ja lämpötila
def get_weather():
    coordinates = get_coordinates(city_name)
    lat = coordinates[0]
    lon = coordinates[1]

    # haetaan rajapinnasta sään nimi ja lämpötila Celsius-asteina
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    response = test_errors(url)
    response_body = response.json()

    weather_name = (response_body["weather"][0]["description"])
    temperature = (response_body["main"]["temp"])
    print(f"Weather in {city_name}: {weather_name}")
    print(f"Temperature: {temperature} degrees Celsius")

# testataan, onko syötteessä numeroita
def test_if_input_has_numbers(city_name):
    numbers = "0123456789"
    is_number = False

    for i in city_name:
        if i in numbers:
            is_number = True
            break
    return is_number

# pääohjelma
city_name = input("Input city name: ")
is_number = test_if_input_has_numbers(city_name)

# kysytään syöte uudelleen, jos käyttäjä syöttää numeroita
while is_number:
    print("Invalid input.")
    city_name = input("Input city name: ")
    is_number = test_if_input_has_numbers(city_name)

get_weather()
