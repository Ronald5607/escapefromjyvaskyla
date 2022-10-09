from geopy import distance
import math
import mysql.connector


class Pelaaja:
    def __init__(self, nimi: str, yhteys): #pelaajalle pitää alustaa nimi (esim (input("Nimi: "))ja aloituspaikka
        self.nimi = nimi
        self.yhteys = yhteys
        self.lentokentan_nimi = 'Jyväskylä Airport'
        self.sijainti = 'EFJY' #jos haluaa sisältää aseman nimen tähän, voisi sijainnin muuntaa esim. tupleksi jossa on ident ja nimi
        self.viimeisimmat = []
        self.lahimmat = []
        self.hae_lahimmat()

    def siirry(self, inputti):
        self.viimeisimmat.append(self.sijainti)
        if len(self.viimeisimmat) == 10:
            self.viimeisimmat.remove(self.viimeisimmat[0])

        self.hae_lahimmat()
        #pelaajan sijainti vaihtuu pelaajan valitseman numeron (indeksin) mukaan
        komento = int(inputti)
        self.sijainti = self.lahimmat[komento - 1][0]
        self.lentokentan_nimi = self.lahimmat[komento - 1][1]

        self.hae_lahimmat()

    def teleportti(self):
        self.viimeisimmat.append(self.sijainti)
        if len(self.viimeisimmat) == 10:
            self.viimeisimmat.remove(self.viimeisimmat[0])

        kursori = self.yhteys.cursor()
        kursori.execute(f"SELECT ident, name FROM airport WHERE iso_country='FI' ORDER BY RAND () LIMIT 1")
        tmp = kursori.fetchone()
        self.sijainti = tmp[0]
        self.lentokentan_nimi = tmp[1]

        self.hae_lahimmat()

    def suunta(self, icao):
        lat1, long1,a ,b = self.hae_tiedot(self.sijainti)
        lat2, long2,a ,b = self.hae_tiedot(icao)

        x = lat2 - lat1
        y = long2 - long1
        brng = math.atan2(x, y)
        brng = math.degrees(brng)

        if brng < 0:
            brng = brng + 360

        print(brng)

        if 22.5 < brng < 67.5:
            return 'Koillisessa'
        elif 67.5 <= brng <= 112.5:
            return 'Pohjoisessa'
        elif 112.5 < brng < 157.5:
            return 'Luoteessa'
        elif 157.5 <= brng <= 202.5:
            return 'Lännessä'
        elif 202.5 < brng < 247.5:
            return 'Lounaassa'
        elif 247.5 <= brng <= 292.5:
            return 'Etelässä'
        elif 292.5 < brng < 337.5:
            return 'Kaakossa'
        elif 337.5 <= brng <= 360 or 0 <= brng <= 22.5:
            return 'Idässä'

    def hae_top5(self):
        sql = 'SELECT name, points FROM peli ORDER BY points DESC limit 5;'
        kursori = self.yhteys.cursor()
        kursori.execute(sql)
        return kursori.fetchall()


    def luo_taulu(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS peli (
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    name CHAR(30) NOT NULL,
    points INT NOT NULL,
    PRIMARY KEY (id))'''
        kursori = self.yhteys.cursor()
        kursori.execute(sql)
    def tallenna_pisteet(self, pisteet):
        kursori = self.yhteys.cursor()
        kursori.execute(f"INSERT INTO peli (name, points) VALUES ('{self.nimi}', {pisteet})")

    def hae_lahimmat(self):
        # hakee nykyisen sijainnin koordinaatit
        kursori = self.yhteys.cursor()
        kursori.execute(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{self.sijainti}'")
        koordinaatit_nykyinen = kursori.fetchone()
        # hakee muiden lentokenttien koordinaatit (hakee aina kaikkien, jos keksii miten simppelisti optimoida tätä eteenpäin niin go ahead)
        kursori.execute(
            f"SELECT ident, name, latitude_deg, longitude_deg FROM airport WHERE iso_country='FI' and ident!='{self.sijainti}'")
        kaikki_asemat = kursori.fetchall()
        # tallettaa listoihin etäisyydet ja asemien tiedot, paitsi ne jotka on kiellettyjen listalla
        etaisyydet = []
        asemat = []
        for asema in kaikki_asemat:
            # luo listan asemista jotka eivät kuulu viimeisimpiin ja laskee niiden etäisyydet nykyisestä
            if asema[0] not in self.viimeisimmat:
                koordinaatit_uusi = (asema[2], asema[3])
                etaisyys = (distance.great_circle(koordinaatit_nykyinen, koordinaatit_uusi).km)
                etaisyydet.append(float(etaisyys))
                asemat.append([asema[0], asema[1], asema[2], asema[3], etaisyys])
        # etaisyydet sortataan pienimmästä suurimpaan
        etaisyydet.sort()
        valittavat = []
        for asema in asemat:
            # hakee lentokentät, joiden etaisyys on top 5 pienimmistä, ja lisää ne listaan valittavat
            # jos etaisyys matchaa, niin kyseessä on tod näk sama lentokenttä. jos pelkää overlappia niin voidaan keksii tähän jotain muuta
            if asema[4] in etaisyydet[0:5]:
                asema.append(self.suunta(asema[0]))
                valittavat.append(asema)
        self.lahimmat = valittavat

    def hae_tiedot(self, icao):
        kursori = self.yhteys.cursor()
        kursori.execute(f"SELECT latitude_deg, longitude_deg, elevation_ft, type FROM airport WHERE ident='{icao}'")
        return kursori.fetchone()


if __name__ == '__main__':
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='roni',
        charset="utf8",
        autocommit=True)

    pelaaja = Pelaaja('aa', yhteys)

    print(pelaaja.suunta('EFHK'))
    print(pelaaja.lahimmat)