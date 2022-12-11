from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from database import Database
import requests
import json
from pelaaja import Pelaaja
from peli import Peli

app = Flask(__name__)
cors = CORS(app)
db = Database() #testausta varten check out database.py


@app.route('/weather/<icao>')
#hakee sään icao koodin perusteella
#linkki: http://127.0.0.1:3000/weather/(icao) -> palauttaa pilvisyyden määrän
#for now laitoin databaseen muistiin myös api keyn. idk
def weather(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident='" + icao + "'"
    kursori = db.get_connection().cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    if not tulos:
        vastaus = "ICAO-koodi on syötetty väärin."
    else:
        lat = tulos[0]
        #print(lat)
        lon = tulos[1]
        #print(lon)
        weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={db.apikey}").json()
        vastaus = {
            "cloudiness": weather["clouds"]["all"]
        }
    return vastaus

@app.route("/name", methods=["POST"])
#hakee index sivulta javascriptillä lähetetyn pelaajan nimen
#ei hyväksyny ku koitin pyörittää tätä laittamal app.runiin localhostin mut ilman hostin määritystä toimii
def get_name():
    dict_name = request.get_json()
    player_name = dict_name["name"]
    print(player_name) #tässä pitäis tulostua pythoniin pelaajan nimi
    #tässä voi tehdä nyt jotain sillä nimellä niiku vaik inserttaa se databaseen
    return player_name


@app.route('/siirto')
def siirto():
    jsoni = request.get_json()
    icao = jsoni['ICAO']
    iidee = jsoni['ID']
    kaydyt = jsoni['kaydyt']

    sql = f"select screen_name from player where ID='{iidee}'"
    kursori = db.get_connection().cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()


    pelaaja = Pelaaja(tulos[0], db)
    pelaaja.viimeisimmat = kaydyt
    pelaaja.siirry(icao)
    pelaaja.hae_lahimmat()

    peli = Peli()
    peli.hae_viholliset()
    peli.hae_hp()
    peli.hae_polttoaine()

    for vihollinen in peli.viholliset:
        vihollinen.siirron_lasku()
        if vihollinen.siirrot == 0:
            peli.hp -= 1
        
    peli.tuhoa_vihollinen()
    peli.polttoaine -= 10

    vastaus = {
    'lahimmat': pelaaja.lahimmat,
    'viholliset': peli.tee_vihollislista(),
    'polttoaine': peli.hae_polttoaine,
    'hp': peli.hp
}







@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus={
        "viesti": "Päätepistettä ei löydy",
        "status": 404
    }
    json_vastaus=json.dumps(vastaus)
    http_vastaus=Response(response=json_vastaus, status=404, mimetype="application/json")
    return http_vastaus

if __name__ == '__main__':
    app.run(port=3000)