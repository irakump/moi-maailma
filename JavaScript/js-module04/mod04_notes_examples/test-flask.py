from Flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

@app.route("/airport/<icao>")
def airport(icao):
    return {"ICAO": icao, "Name": "Airport name"}

app.run()
