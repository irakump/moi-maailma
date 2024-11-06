from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def hello():
    return "Heippahei, serveri tervehtii sinua!"

# http://127.0.0.1:3000/summa?luku1=13&luku2=28

# tämä on päätepiste eli route      # harvinaisempi tapa (nykyaikainen tapa on käyttää /-merkkejä eikä esim. ?q=)
@app.route('/summa')
def summa():
    args = request.args
    luku1 = float(args.get("luku1"))
    luku2 = float(args.get("luku2"))
    summa = luku1+luku2

    vastaus = {
        "luku1": luku1,
        "luku2": luku2,
        "summa": summa
    }

    return vastaus

    #return str(summa)
    #return "Summa tervehtii sinua!"

@app.route('/kaiku/<teksti>')
def kaiku(teksti):

    vastaus = {
        "kaiku": teksti + " " + teksti
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)     # ip-osoite 127.0.0.1 = localhost


