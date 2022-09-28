import pelaaja
import vihollinen


class Peli:
    def __init__(self, gamer):
        self.pelaaja = gamer
        self.viholliset = []
        self.pisteet = 0

    def lisaa_vihollinen(self):
        ...

    def lisaa_pisteita(self):
        ...

    def havio(self):
        ...

