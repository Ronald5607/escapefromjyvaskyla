from random import randint


class Vihollinen:
    tyypit = {'jäämies': ('longitude', 'cc'),
              'tuliukko': ('longitude', 'dd'),
              'peukaloinen': 'large_airport',
              'jättiläinen': 'small_airport',
              'hujoppi': ('elevation_ft', 'aa'),
              'pätkä': ('elevation_ft', 'bb')}

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
            self.tyyppi = 'peukaloinen'  # 0,5 %
        elif rnd_num <= 225:
            self.tyyppi = 'jättiläinen'  # 22%
        elif rnd_num <= 415:
            self.tyyppi = 'jäämies'  # 19,5%
        elif rnd_num <= 610:
            self.tyyppi = 'tuliukko'  # 19%
        elif rnd_num <= 805:
            self.tyyppi = 'hujoppi'  # 19,5%
        elif rnd_num <= 1000:
            self.tyyppi = 'pätkä'  # 19,5%

    def anna_heikkous(self):
        self.heikkous = self.tyypit[self.tyyppi]

    def anna_siirrot(self):
        if self.tyyppi == 'peukaloinen':
            self.siirrot = 41
        elif self.tyyppi == 'jättiläinen':
            self.siirrot = 16
        elif self.tyyppi == 'jäämies':
            self.siirrot = 16
        elif self.tyyppi == 'tuliukko':
            self.siirrot = 11
        elif self.tyyppi == 'hujoppi':
            self.siirrot = 16
        elif self.tyyppi == 'pätkä':
            self.siirrot = 16

    def anna_pisteet(self):
        if self.tyyppi == 'peukaloinen':
            self.pistemaara = 5000
        elif self.tyyppi == 'jättiläinen':
            self.pistemaara = 100
        elif self.tyyppi == 'jäämies':
            self.pistemaara = 100
        elif self.tyyppi == 'tuliukko':
            self.pistemaara = 100
        elif self.tyyppi == 'hujoppi':
            self.pistemaara = 100
        elif self.tyyppi == 'pätkä':
            self.pistemaara = 100


if __name__ == '__main__':
    ...
    # a = Vihollinen(3, 7)
    # print(a.tyyppi)