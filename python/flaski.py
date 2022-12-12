from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from database import Database
import requests
import json
from pelaaja import Pelaaja
from peli import Peli
from vihollinen import Vihollinen

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



""" @app.route('/weather/<icao>')
#hakee sään icao koodin perusteella
#linkki: http://127.0.0.1:3000/weather/(icao) -> palauttaa pilvisyyden määrän
#for now laitoin databaseen muistiin myös api keyn. idk """

def weather(icao):
    db = Database()
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
        vastaus = weather["clouds"]["all"]
    return vastaus

@app.route("/name", methods=['POST'])
#hakee index sivulta javascriptillä lähetetyn pelaajan nimen
#ei hyväksyny ku koitin pyörittää tätä laittamal app.runiin localhostin mut ilman hostin määritystä toimii
def get_name():
    db = Database()
    dict_name = request.args
    player_name = dict_name.get('name')

        

    sql = f"insert into player (screen_name,points,hp,fuel) values ('{player_name}',0,3,100)"
    kursori = db.connection.cursor(buffered=True)
    kursori.execute(sql)
    sql = f"select ID from player where screen_name='{player_name}'"
    kursori.execute(sql)
    iidee = kursori.fetchone()[0]

    uusi_peli = Peli(iidee, db.connection)
    uusi_peli.lisaa_vihollinen(5)
    sql = f"insert into enemy (e1,e2,e3,e4,e5,e1_moves,e2_moves,e3_moves,e4_moves,e5_moves) values ('{uusi_peli.viholliset[0].tyyppi}','{uusi_peli.viholliset[1].tyyppi}','{uusi_peli.viholliset[2].tyyppi}','{uusi_peli.viholliset[3].tyyppi}','{uusi_peli.viholliset[4].tyyppi}',{uusi_peli.viholliset[0].siirrot},{uusi_peli.viholliset[1].siirrot},{uusi_peli.viholliset[2].siirrot},{uusi_peli.viholliset[3].siirrot},{uusi_peli.viholliset[4].siirrot})"
    kursori.execute(sql)

    lahimmat = [
        [
            "EFHA",
            "Halli Airport",
            61.856,
            24.7867,
            76.15986038241324,
            "Lounaassa",
            100
        ],
        [
            "EFHI",
            "Haapamä¤ki Airfield",
            62.2552,
            24.3495,
            70.47034696457746,
            "Lännessä",
            100
        ],
        [
            "EFJV",
            "Central Finland Central Hospital Heliport",
            62.2304,
            25.7115,
            18.881154808780686,
            "Etelässä",
            100
        ],
        [
            "EFPK",
            "Pieksämäki Airfield",
            62.2647,
            27.0028,
            70.00990795049564,
            "Idässä",
            100
        ],
        [
            "FI-0005",
            "Mänttä - Sassi Airfield",
            62.028,
            24.664,
            66.86299173741165,
            "Lännessä",
            100
        ]
    ]

    uusi_peli.hp = 3
    uusi_peli.polttoaine = 100
    uusi_peli.pisteet = 0
    uusi_peli.tietokanta_siirto()

    viholliset = uusi_peli.tee_vihollislista()

    vastaus = {
        'lahimmat': lahimmat,
        'ID': iidee,
        'viholliset': viholliset
    }

    return vastaus


@app.route('/siirto')
def siirto():
    db = Database()
    args = request.args
    icao = args.get('ICAO')
    iidee = int(args.get('ID'))
    kaydyt = args.get('kaydyt')
    kaydyt = kaydyt.split(',')

    sql = f"select screen_name from player where ID='{iidee}'"
    kursori = db.get_connection().cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()


    pelaaja = Pelaaja(tulos[0], db.connection)
    pelaaja.viimeisimmat = kaydyt
    pelaaja.sijainti = icao
    pelaaja.hae_lahimmat()
    for lahin in pelaaja.lahimmat:
        lahin.append(weather(lahin[0]))

    peli = Peli(iidee, db.connection)
    peli.hae_viholliset()
    peli.hae_hp()
    peli.hae_polttoaine()

    for vihollinen in peli.viholliset:
        vihollinen.siirron_lasku()
        if vihollinen.siirrot == 0:
            peli.hp -= 1
        
    peli.tuhoa_vihollinen(icao, pelaaja)
    peli.polttoaine -= 10

    peli.tietokanta_siirto()


    vastaus = {
    'lahimmat': pelaaja.lahimmat,
    'viholliset': peli.tee_vihollislista(),
    'polttoaine': peli.polttoaine,
    'hp': peli.hp
    }

    return vastaus







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
    app.run(port=8888)