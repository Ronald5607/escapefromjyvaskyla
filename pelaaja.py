from geopy import distance


class Pelaaja:
    def __init__(self, nimi: str): #pelaajalle pitää alustaa nimi (esim (input("Nimi: "))ja aloituspaikka
        self.nimi = nimi
        self.lentokentan_nimi = 'Jyväskylä Airport'
        self.sijainti = 'EFJY' #jos haluaa sisältää aseman nimen tähän, voisi sijainnin muuntaa esim. tupleksi jossa on ident ja nimi
        self.viimeisimmat = []
        self.lahimmat = []

    def siirry(self, yhteys, inputti):
        #lisää nykyisen sijainnin kiellettyjen listaan viimeiseksi ja poistaa ensimmäisen alkion
        self.viimeisimmat.append(self.sijainti)
        if len(self.viimeisimmat) == 10:
                self.viimeisimmat.remove(self.viimeisimmat[0])
        #hakee nykyisen sijainnin koordinaatit
        kursori = yhteys.cursor()
        kursori.execute(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{self.sijainti}'")
        koordinaatit_nykyinen=kursori.fetchone()
        #hakee muiden lentokenttien koordinaatit (hakee aina kaikkien, jos keksii miten simppelisti optimoida tätä eteenpäin niin go ahead)
        kursori.execute(f"SELECT ident, name, latitude_deg, longitude_deg FROM airport WHERE iso_country='FI' and ident!='{self.sijainti}'")
        kaikki_asemat = kursori.fetchall()
        # tallettaa listoihin etäisyydet ja asemien tiedot, paitsi ne jotka on kiellettyjen listalla
        etaisyydet = []
        asemat=[]
        for asema in kaikki_asemat:
            #luo listan asemista jotka eivät kuulu viimeisimpiin ja laskee niiden etäisyydet nykyisestä
            if asema[0] not in self.viimeisimmat:
                koordinaatit_uusi = (asema[2], asema[3])
                etaisyys = (distance.great_circle(koordinaatit_nykyinen, koordinaatit_uusi).km)
                etaisyydet.append(float(etaisyys))
                asemat.append((asema[0], asema[1], asema[2], asema[3], etaisyys))
        #etaisyydet sortataan pienimmästä suurimpaan
        etaisyydet.sort()
        valinta_numero = 1
        valittavat = []
        for asema in asemat:
            #hakee lentokentät, joiden etaisyys on top 5 pienimmistä, ja lisää ne listaan valittavat
            #jos etaisyys matchaa, niin kyseessä on tod näk sama lentokenttä. jos pelkää overlappia niin voidaan keksii tähän jotain muuta
            if asema[4] in etaisyydet[0:5]:
              # print(f"{valinta_numero}: {asema[1]}")
                valittavat.append(asema)
                valinta_numero += 1
        #pelaajan sijainti vaihtuu pelaajan valitseman numeron (indeksin) mukaan
        #komento = int(input("Valitse aseman numero jonne lennetään: "))
        komento = int(inputti)
        self.sijainti = valittavat[komento - 1][0]
        self.lentokentan_nimi = self.sijainti = valittavat[komento - 1][1]
        self.lahimmat = valittavat

    def teleport(self):
        ...

    def kaukolento(self):
        ...
