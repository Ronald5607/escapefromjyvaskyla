from random import randint


class Vihollinen:
    tyypit = {'iceman': ('longitude', 'cc'),
              'tuliukko': ('longitude', 'dd'),
              'pieni': 'large_airport',
              'iso': 'small_airport',
              'pitka': ('elevation_ft', 'aa'),
              'lyhyt': ('elevation_ft', 'bb')}

    def __init__(self):
        # tyyppi käyttää metodia tyypin_todennäköisyys() määrittääkseen tyypin
        self.tyyppi = 0
        self.anna_tyyppi()
        # siirtojen määrä riippuu tyypistä
        self.siirrot = 0
        self.anna_siirrot()
        # heikkous riippuu tyypistä
        self.heikkous = 0
        self.anna_heikkous()
        # pistemäärä riippuu tyypistä
        self.pistemaara = 0
        self.anna_pisteet()

    def siirron_lasku(self):
        if self.siirrot > 0:
            self.siirrot -= 1

    def anna_tyyppi(self):
        rnd_num = randint(1, 1000)

        if rnd_num <= 5:
            self.tyyppi = 'pieni'  # 0,5 %
        elif rnd_num <= 225:
            self.tyyppi = 'iso'  # 22%
        elif rnd_num <= 415:
            self.tyyppi = 'iceman'  # 19,5%
        elif rnd_num <= 610:
            self.tyyppi = 'tuliukko'  # 19%
        elif rnd_num <= 805:
            self.tyyppi = 'pitka'  # 19,5%
        elif rnd_num <= 1000:
            self.tyyppi = 'lyhyt'  # 19,5%

    def anna_heikkous(self):
        self.heikkous = self.tyypit[self.tyyppi]

    def anna_siirrot(self):
        if self.tyyppi == 'pieni':
            self.siirrot = 20
        elif self.tyyppi == 'iso':
            self.siirrot = 10
        elif self.tyyppi == 'iceman':
            self.siirrot = 10
        elif self.tyyppi == 'tuliukko':
            self.siirrot = 10
        elif self.tyyppi == 'pitka':
            self.siirrot = 10
        elif self.tyyppi == 'lyhyt':
            self.siirrot = 10

    def anna_pisteet(self):
        if self.tyyppi == 'pieni':
            self.pistemaara = 5000
        elif self.tyyppi == 'iso':
            self.pistemaara = 100
        elif self.tyyppi == 'iceman':
            self.pistemaara = 100
        elif self.tyyppi == 'tuliukko':
            self.pistemaara = 100
        elif self.tyyppi == 'pitka':
            self.pistemaara = 100
        elif self.tyyppi == 'lyhyt':
            self.pistemaara = 100


if __name__ == '__main__':
    ...
    # a = Vihollinen(3, 7)
    # print(a.tyyppi)