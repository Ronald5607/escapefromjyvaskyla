from flask import Flask, Response
from flask_cors import CORS
import requests
import json

apikey = "" #testausta varten voi lisätä tähän apikeyn
salasana = "" #testausta varten voi lisätä tähän salasanan
tietokanta = 'flight_game'
käyttäjä = 'root'

app = Flask(__name__)
CORS(app)

#hakee sään icao koodin perusteella
#linkki: http://127.0.0.1:3000/weather/(icao) -> palauttaa pilvisyyden määrän
@app.route('/weather/<icao>')
def weather(icao):
    import mysql.connector
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database=tietokanta,
        user=käyttäjä,
        password=salasana,
        autocommit=True)
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident='" + icao + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    if not tulos:
        vastaus = "ICAO-koodi on syötetty väärin."
    else:
        lat = tulos[0]
        lon = tulos[1]
        weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}").json()
        vastaus = {
            "cloudiness": weather["clouds"]["all"]
        }
    return vastaus

# @app.errorhandler(404)
# def page_not_found(virhekoodi):
#     vastaus={
#         "viesti": "Päätepistettä ei löydy",
#         "status": 404
#     }
#     json_vastaus=json.dumps(vastaus)
#     http_vastaus=Response(response=json_vastaus, status=404, mimetype="application/json")
#     return http_vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)