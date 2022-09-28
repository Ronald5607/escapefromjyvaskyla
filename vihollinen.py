from random import randint


class Vihollinen:
    tyypit = {'iceman': ('longitude', 'cc'),
              'tuliukko': ('longitude', 'dd'),
              'pieni': 'large_airport',
              'iso': 'small_airport',
              'pitka': ('elevation_ft', 'aa'),
              'lyhyt': ('elevation_ft', 'bb')}

    def __init__(self, tyyppimaara):
        # tyyppi käyttää metodia tyypin_todennäköisyys() määrittääkseen tyypin
        self.tyyppi = []
        # siirtojen määrä riippuu tyypistä
        self.siirrot = 0
        # heikkous riippuu tyypistä
        self.heikkous = []

    def siirron_lasku(self):
        if self.siirrot > 0:
            self.siirrot -= 1

    def tyypin_todennakoisyys(self):
        ...


if __name__ == '__main__':
    ...
    # a = Vihollinen(3, 7)
    # print(a.tyyppi)