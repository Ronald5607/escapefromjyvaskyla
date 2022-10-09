import pelaaja
import peli
import screen
import vihollinen
from random import randint

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
         charset="utf8",
         autocommit=True)

ikkuna = screen.Screen(150, 40)

nimetty = False
ikkuna.clear()
ikkuna.draw_text_box(ikkuna.center[0], ikkuna.center[1], 'Anna nimi:', 'Max 10 kirjainta')
ikkuna.flush()
while not nimetty:
    nimi = input()
    if len(nimi) <= 10:
        nimetty = True
    else:
        ikkuna.clear()
        ikkuna.draw_text_box(ikkuna.center[0], ikkuna.center[1],'Nimesi on liian pitkä', 'Anna nimi:')
        ikkuna.flush()

pelaaja = pelaaja.Pelaaja(nimi, yhteys)
peli = peli.Peli(pelaaja)

# vihollisten lisäys
peli.lisaa_vihollinen(5)


havinnyt = False

while not havinnyt:

    ikkuna.get_size()
    ikkuna.clear()


    ikkuna.draw_text_box(ikkuna.top_right[0] - 13, ikkuna.top_right[1], 'Pisteet:', str(peli.pisteet))

    ikkuna.draw_text_box(ikkuna.top_left[0] + 10, ikkuna.center[1], pelaaja.lentokentan_nimi)



    ikkuna.draw_text_box(ikkuna.top_left[0], ikkuna.bottom_left[1] - 10,
                         pelaaja.lahimmat[0][1],
                         pelaaja.lahimmat[1][1],
                         pelaaja.lahimmat[2][1],
                         pelaaja.lahimmat[3][1],
                         pelaaja.lahimmat[4][1])

    peli.tuhoa_vihollinen(pelaaja.sijainti, pelaaja)
    print(pelaaja.hae_tiedot(pelaaja.sijainti))
    i = 0
    for vihollinen in peli.viholliset:

        vihollinen.siirron_lasku()
        if vihollinen.siirrot == 1:
            havinnyt = True
        i += 1
        ikkuna.draw_text(ikkuna.center[0] + 20, ikkuna.center[1] + i, vihollinen.tyyppi + str(vihollinen.siirrot))

    ikkuna.flush()

    komento = input('mitä teet: ')
    if komento == 'lopeta':
        havinnyt = True
    elif komento == '1':
        pelaaja.siirry(1)
    elif komento == '2':
        pelaaja.siirry(2)
    elif komento == '3':
        pelaaja.siirry(3)
    elif komento == '4':
        pelaaja.siirry(4)
    elif komento == '5':
        pelaaja.siirry(5)
    elif komento == 'teleport':
        if peli.pisteet > 200:
            pelaaja.teleportti()
            peli.pisteet -= 200
        else:
            ...

ikkuna.clear()
ikkuna.draw_text_box(ikkuna.center[0] - 13, ikkuna.center[1], 'HÄVISIT PELIN(ILKKA ANNA VITONEN)')
ikkuna.flush()
aa = True

