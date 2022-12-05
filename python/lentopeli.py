import pelaaja
import peli
import screen

import mysql.connector

ikkuna = screen.Screen(180, 50)
ikkuna.clear()
ikkuna.draw_text_box(ikkuna.center[0] - len('Anna tietokannan salasana:')//2, ikkuna.center[1], 'Anna tietokannan salasana:')
ikkuna.flush()
salasana = input()

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password=salasana,
         autocommit=True)


ikkuna.clear()

# nimen anto
ikkuna.draw_text_box(ikkuna.center[0] - len('Max 10 kirjainta')//2, ikkuna.center[1], 'Anna nimi:', 'Max 10 kirjainta')
ikkuna.flush()

nimetty = False
while not nimetty:
    nimi = input()
    if len(nimi) <= 10:
        nimetty = True
    else:
        ikkuna.clear()
        ikkuna.draw_text_box(ikkuna.center[0], ikkuna.center[1],'Nimesi on liian pitkä', 'Anna nimi:')
        ikkuna.flush()

# lore ruutu ja pelin aloitus
vastattu = False
while not vastattu:
    ikkuna.clear()
    ikkuna.draw_text_box(ikkuna.top_left[0] + 60, ikkuna.top_left[1] + 3, 'Escape from Jyväskylä')
    ikkuna.draw_text_box(ikkuna.top_left[0] + 22, ikkuna.top_left[1] + 5,
                         f'Terve {nimi}, sinulle on tarjottu tehtäväksi pitää Projekti Maailman Pelastaja turvassa.',
                         'Kohdetta pidetään piilossa Jyväskylän tukikohdassa, mutta tuhonhimoiset kapitalistit ovat',
                         'jo paikantaneet sen ja matkalla tuhoamaan sitä. Sinun tulee ottaa Projekti Maailman',
                         'Pelastaja ja lentää sillä karkuun. Koska se ei kaipaa muuta polttoainetta kuin vesihöyryä,',
                         'pystyt lentämään sillä loputtomasti kunhan vaan joskus lennät pilvien läpi. Vaadimme',
                         'sinun suojelevan sitä hengelläsi. Otatko tehtävän vastaan?')
    ikkuna.draw_text_box(ikkuna.top_left[0] + 22, ikkuna.top_left[1] + 15,
                         'Sinun tulee karkoittaa kapitalisti siat kannoiltasi ennen kuin he pääsevät käsiksi Projekti',
                         'Maailman Pelastajaan. Eri kapitalisteilla on eri heikkouksia, ja sinun tulee hyödyntää niitä,',
                         'jotta pääset heistä eroon.',
                         'Painamalla numeroita 1-5 pystyt valitsemaan, minne lähimmistä lentokentistä haluat',
                         'lentää. Jos haluat käyttää Projekti Maailman Pelastajan teleportti-toimintoa, paina 6. Pidä',
                         'mielessä, että teleportti on vielä prototyyppivaiheessa eikä sillä siksi pysty vaikuttamaan',
                         'siihen, mihin se teleporttaa. Teleportin käynnistämiseen tarvitset 200 pistettä, ja jos sinulla',
                         'ei riitä pisteet, niin älä tuhlaa aikaasi sen yrittämiseen.')
    ikkuna.draw_airplane(ikkuna.center[0] - 5, ikkuna.bottom_left[1] - 5)
    ikkuna.flush()
    vastaus = input('Oletko valmis aloittamaan? Kirjoita \'kyllä\'... tai \'ei\'...: ')
    if vastaus == 'kyllä':
        vastattu = True
    elif vastaus == 'ei':
        raise ValueError('nössö')


pelaaja = pelaaja.Pelaaja(nimi, yhteys)
peli = peli.Peli(pelaaja)

# vihollisten lisäys
peli.lisaa_vihollinen(5)

havinnyt = False
while not havinnyt:

    ikkuna.get_size()
    ikkuna.clear()

    ikkuna.draw_text_box(ikkuna.top_right[0] - 13, ikkuna.top_right[1] + 1, 'Pisteet:', str(peli.pisteet))

    tmp = len(pelaaja.lentokentan_nimi)
    ikkuna.draw_text_box(ikkuna.center[0] - tmp//2, ikkuna.center[1], pelaaja.lentokentan_nimi)

    k = 0
    z = 0
    for lahin in pelaaja.lahimmat:
        tiedot = pelaaja.hae_tiedot(lahin[0])
        if z < 3:
            ikkuna.draw_text_box(ikkuna.center[0] + k - 40, ikkuna.top_right[1] + 2,
                                 'Valinta ' + str(z + 1),
                                 lahin[1],
                                 'Korkeus: ' + str(tiedot[2]) + ' ft',
                                 'Suunta: ' + str(lahin[5]),
                                 'Tyyppi: ' + str(tiedot[3]).replace('_', ' '))
            if z == 2:
                k = 0
        else:
            ikkuna.draw_text_box(ikkuna.center[0] + k - 30, ikkuna.top_right[1] + 8,
                                 'Valinta ' + str(z + 1),
                                 lahin[1],
                                 'Korkeus: ' + str(tiedot[2]) + ' ft',
                                 'Suunta: ' + str(lahin[5]),
                                 'Tyyppi: ' + str(tiedot[3]).replace('_', ' '))
        if z != 2:
            k += max(len('Korkeus: ' + str(tiedot[2]) + ' ft'),
                     len('Valinta ' + str(z + 1)),
                     len('Suunta: ' + str(lahin[5])),
                     len('Tyyppi: ' + str(tiedot[3])),
                     len(lahin[1])) + 3
        z += 1
    if peli.pisteet >= 200:
        ikkuna.draw_text_box(ikkuna.center[0] + k - 30, ikkuna.top_right[1] + 8, 'Valinta 6', 'Teleport')

    ikkuna.draw_airplane(ikkuna.center[0] - 5, ikkuna.center[1] - 3)

    if peli.pisteet >= 200:
        ikkuna.draw_text_box(5, ikkuna.bottom_left[1] - 10,
                             'Kirjoita komento jonka haluat suorittaa.',
                             'Komento 1-5: lennä kyseiselle kentälle.',
                             'komento 6: siirryt satunnaiselle kentälle.',
                             'Komento lopeta: lopettaa pelin.')
    else:
        ikkuna.draw_text_box(5, ikkuna.bottom_left[1] - 10,
                             'Kirjoita komento jonka haluat suorittaa.',
                             'Komento 1-5: lennä kyseiselle kentälle.',
                             'Komento lopeta: lopettaa pelin.')

    peli.viholliset.sort(key=lambda x: x.siirrot)
    k = 0
    for vihollinen in peli.viholliset:

        vihollinen.siirron_lasku()
        if vihollinen.siirrot == 1:
            havinnyt = True

        ikkuna.draw_text_box(ikkuna.center[0] + k - 40, ikkuna.center[1] + 6, vihollinen.tyyppi,
                             'Etäisyys: ' + str(vihollinen.siirrot))
        k += max(len(vihollinen.tyyppi), len('Etäisyys: ' + str(vihollinen.siirrot))) + 3
    ikkuna.flush()
    komento = input('mitä teet: ')
    if komento == 'lopeta':
        havinnyt = True
    elif komento == '1':
        pelaaja.siirry(1)
        peli.tuhoa_vihollinen(pelaaja.sijainti, pelaaja)
    elif komento == '2':
        pelaaja.siirry(2)
        peli.tuhoa_vihollinen(pelaaja.sijainti, pelaaja)
    elif komento == '3':
        pelaaja.siirry(3)
        peli.tuhoa_vihollinen(pelaaja.sijainti, pelaaja)
    elif komento == '4':
        pelaaja.siirry(4)
        peli.tuhoa_vihollinen(pelaaja.sijainti, pelaaja)
    elif komento == '5':
        pelaaja.siirry(5)
        peli.tuhoa_vihollinen(pelaaja.sijainti, pelaaja)
    elif komento == '6':
        if peli.pisteet >= 200:
            pelaaja.teleportti()
            peli.tuhoa_vihollinen(pelaaja.sijainti, pelaaja)
            peli.pisteet -= 200
        else:
            pass

pelaaja.luo_taulu()
pelaaja.tallenna_pisteet(peli.pisteet)

ikkuna.clear()
ikkuna.draw_text_box(ikkuna.center[0] - 13, ikkuna.center[1], 'HÄVISIT PELIN(ANNA VITONEN)')
top5 = pelaaja.hae_top5()
i = 0
j = 0
for pelaaja in top5:
    ikkuna.draw_text_box(ikkuna.center[0] + i - 14, ikkuna.center[1] + 5, str(pelaaja[0]), str(pelaaja[1]))
    i += max(len(str(pelaaja[0])), len(str(pelaaja[1]))) + 3
    j += 1

ikkuna.flush()



