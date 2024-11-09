# Tehtävä 13.2
# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin
# JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava
# GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa:
# {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask, Response
import json
import mysql.connector

app = Flask(__name__)

@app.route("/airport/<icao>")

def get_name_and_municipality(icao):

    # virheiden käsittely
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='ira',
            password='lunni',
            autocommit=True,
            charset='utf8mb4',
            collation='utf8mb4_general_ci'
        )

        sql = f'SELECT ident, name, municipality FROM airport WHERE ident = "{icao}";'
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()

        status_code = 200
        answer = {
            "ICAO": result[0],
            "Name": result[1],
            "Municipality": result[2]
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
