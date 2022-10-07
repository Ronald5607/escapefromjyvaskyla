import pelaaja
import vihollinen


class Peli:
    def __init__(self, gamer):
        self.pelaaja = gamer
        self.viholliset = []
        self.pisteet = 0
        self.havinnyt = False

    def lisaa_vihollinen(self):
        self.viholliset.append(vihollinen.Vihollinen)

    def tuhoa_vihollinen(self):
        for vihollinen in self.viholliset:
            ...

    def lisaa_pisteita(self):
        ...

    def havio(self):
        for vihollinen in self.viholliset:
            if vihollinen.siirrot <= 0:
                self.havinnyt = True

