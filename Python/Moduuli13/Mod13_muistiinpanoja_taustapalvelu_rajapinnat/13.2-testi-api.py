# Tehtävä 13.2
# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin
# JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava
# GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa:
# {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask, Response
import requests
import requests.exceptions
import json

api_token = ""      # api_token poistettu

app = Flask(__name__)

@app.route("/airport/<icao>")

def get_name_and_municipality(icao):
    url = f"https://airportdb.io/api/v1/airport/{icao}?apiToken={api_token}"

    # virheiden käsittely
    try:
        response = requests.get(url)
        response_body = response.json()

        status_code = 200
        answer = {
            "ICAO": response_body["ident"],
            "Name": response_body["name"],
            "Municipality": response_body["municipality"]
        }

    except ValueError:
        status_code = 400
        answer = {
            "status": status_code,
            "text": "Invalid ICAO"
        }

    json_answer = json.dumps(answer)
    return Response(response=json_answer, status=status_code, mimetype="application/json")

@app.errorhandler(404)

def page_not_found(error_code):
    answer = {
        "status": "404",
        "text": "Wrong endpoint"
    }

    json_answer = json.dumps(answer)
    return Response(response=json_answer, status=404, mimetype="application/json")

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)

# http://127.0.0.1:3000/airport/efhk
