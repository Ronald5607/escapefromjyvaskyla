import pelaaja
import peli
import screen
import vihollinen

ikkuna = screen.Screen(150, 40)

havinnyt = False

while not havinnyt:

    ikkuna.clear()
    ikkuna.draw_text_box(ikkuna.top_right[0] - 13, ikkuna.top_right[1], 'Pisteet:', str(5003))
    ikkuna.draw_airplane(ikkuna.center[0], ikkuna.center[1])
    ikkuna.flush()

    komento = input('mitä teet: ')
    if komento == 'lopeta':
        havinnyt = True
