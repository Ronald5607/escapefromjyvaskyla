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
            if vihollinen.tyyppi == 'peukaloinen':
                if tiedot[3] == 'large_airport':
                    self.viholliset.remove(vihollinen)
                    self.pisteet += vihollinen.pistemaara
                    break
            elif vihollinen.tyyppi == 'jättiläinen':
                if tiedot[3] == 'small_airport' or tiedot[3] == 'heliport':
                    self.viholliset.remove(vihollinen)
                    self.pisteet += vihollinen.pistemaara
                    break
            elif vihollinen.tyyppi == 'jäämies':
                if tiedot[0] < 62.242603:
                    self.viholliset.remove(vihollinen)
                    self.pisteet += vihollinen.pistemaara
                    break
            elif vihollinen.tyyppi == 'tuliukko':
                if tiedot[0] > 65.012093:
                    self.viholliset.remove(vihollinen)
                    self.pisteet += vihollinen.pistemaara
                    break
            elif vihollinen.tyyppi == 'hujoppi':
                if tiedot[2] < 311:
                    self.viholliset.remove(vihollinen)
                    self.pisteet += vihollinen.pistemaara
                    break
            elif vihollinen.tyyppi == 'pätkä':
                if tiedot[2] > 311:
                    self.viholliset.remove(vihollinen)
                    self.pisteet += vihollinen.pistemaara
                    break
        if len(self.viholliset) < 5:
            self.lisaa_vihollinen(1)


