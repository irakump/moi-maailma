# MODUULI 13 - TAUSTAPALVELUN JA RAJAPINNAN RAKENTAMINEN

# termit: BACKEND, ENDPOINT

# BACKEND = taustapalvelu
# ENDPOINT = HTTP-päätepiste

# taustapalvelu rakennetaan Flask-kirjaston avulla. Flask tarjoaa mahdollisuuden päätepisteiden ohjelmointiin

# yksinkertainen taustapalvelu (serveri)
from flask import Flask, Response
import json

app = Flask(__name__)
@app.route("/summa/<num1>/<num2>")
def summa(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        summa = num1 + num2

        status_code = 200
        response = {
            "status": status_code,                        # vastaus JSON-muodossa
            "num1": num1,
            "num2": num2,
            "summa": summa
        }

    except valueError:
        status_code = 400
        response = {
            "status": status_code,
            "text": "Wrong number"
        }
    json_answer = json.dumps(response)
    return Response(response=json_answer, status=404, mimetype="application/json")

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)

# app.run -metodin kutsu käynnistää taustapalvelun (tätä voidaan kysyä kokeessa?)
# @app.route("summa") määrittää päätepisteen eli kertoo, että seuraavan rivin funktio nimeltä summa ajetaan silloin, kun käyttäjä
    # lähettää pyynnön, jonka ip-osoiteosan jälkeen lukee merkkijono /summa

# JSON = JavaScript Object Notation

# toinen serveri
from flask import Flask

app = Flask(__name__)
@app.route('/kaiku/<teksti>')
def kaiku(teksti):
    vastaus = {
        "kaiku" : teksti + " " + teksti
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

