import pelaaja
import vihollinen


class Peli:
    def __init__(self, gamer):
        self.pelaaja = gamer
        self.viholliset = []
        self.pisteet = 0
        self.havinnyt = False

    def lisaa_vihollinen(self, n):
        for i in range(n):
            self.viholliset.append(vihollinen.Vihollinen())

    def tuhoa_vihollinen(self, sijainti, pelaaja):
        tiedot = pelaaja.hae_tiedot(sijainti)
        for vihollinen in self.viholliset:
            if vihollinen.tyyppi == 'pieni':
                if tiedot[3] == 'large_airport':
                    self.viholliset.remove(vihollinen)
                    break
            elif vihollinen.tyyppi == 'iso':
                if tiedot[3] == 'small_airport' or tiedot[3] == 'heliport':
                    self.viholliset.remove(vihollinen)
                    break
            elif vihollinen.tyyppi == 'iceman':
                if tiedot[0] < 62.242603:
                    self.viholliset.remove(vihollinen)
                    break
            elif vihollinen.tyyppi == 'tuliukko':
                if tiedot[0] > 65.012093:
                    self.viholliset.remove(vihollinen)
                    break
            elif vihollinen.tyyppi == 'pitka':
                if tiedot[2] < 311:
                    self.viholliset.remove(vihollinen)
                    break
            elif vihollinen.tyyppi == 'lyhyt':
                if tiedot[2] > 311:
                    self.viholliset.remove(vihollinen)
                    break
        if len(self.viholliset) < 5:
            self.lisaa_vihollinen(1)

    def lisaa_pisteita(self):
        ...

    def havio(self):
        for vihollinen in self.viholliset:
            if vihollinen.siirrot <= 0:
                self.havinnyt = True

