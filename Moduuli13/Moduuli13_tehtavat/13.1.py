# Tehtävä 13.1
# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei. Hyödynnä toteutuksessa
# aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa:
# http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask, Response
import json

app = Flask(__name__)

@app.route("/prime/<number>")

def prime(number):
    try:
        number = float(number)
        numbers = []
        iterator = 2
        is_prime = False

        while (iterator <= number):
            numbers.append(iterator)
            iterator += 1

        if (number < 1):
            is_prime = False
        elif (number == 1):
            is_prime = True

        for num in numbers:
            if (number % num == 0) and (number // num != 1):     #testataan, onko luku jaollinen muulla kuin itsellään
                is_prime = False
                break
            elif (number % num == 0) and (number // num == 1):   #luku on jaollinen vain itsellään (ja ykkösellä)
                is_prime = True

        status_code = 200
        answer = {
            "Number":number,
            "isPrime":is_prime
        }

    except ValueError:
        status_code = 400
        answer = {
            "status": status_code,
            "text": "Invalid number"
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

# http://127.0.0.1:3000/prime/10
