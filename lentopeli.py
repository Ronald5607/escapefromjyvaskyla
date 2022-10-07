import pelaaja
import peli
import screen
import vihollinen

import mysql.connector
from geopy import distance



ikkuna = screen.Screen(150, 40)
ikkuna.clear()
ikkuna.draw_text_box(ikkuna.center[0], ikkuna.center[1], 'Anna tietokannan salasana:')
ikkuna.flush()
salasana = input()

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password=salasana,
         autocommit=True)

ikkuna = screen.Screen(150, 40)
ikkuna.clear()
ikkuna.draw_text_box(ikkuna.center[0], ikkuna.center[1], 'Anna nimi:')
ikkuna.flush()
nimi = input()
pelaaja = pelaaja.Pelaaja(nimi)
peli = peli.Peli(pelaaja)



havinnyt = False

while not havinnyt:

    ikkuna.get_size()
    ikkuna.clear()


    ikkuna.draw_text_box(ikkuna.top_right[0] - 13, ikkuna.top_right[1], 'Pisteet:', str(5003))

    ikkuna.draw_text_box(ikkuna.center[0] + 10, ikkuna.center[1], pelaaja.lentokentan_nimi)
    siirtyminen = input()
    pelaaja.siirry(yhteys, siirtyminen)

    ikkuna.draw_text_box(ikkuna.top_left[0], ikkuna.bottom_left[1] - 10, pelaaja.lahimmat[0][1],pelaaja.lahimmat[1][1],pelaaja.lahimmat[2][1])

    ikkuna.flush()


    komento = input('mitä teet: ')
    if komento == 'lopeta':
        havinnyt = True
