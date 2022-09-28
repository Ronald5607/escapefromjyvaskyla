from random import randint


class Vihollinen:
    tyypit = {'iceman': ('longitude', 'cc'),
              'tuliukko': ('longitude', 'dd'),
              'pieni': 'large_airport',
              'iso': 'small_airport',
              'pitka': ('elevation_ft', 'aa'),
              'lyhyt': ('elevation_ft', 'bb')}

    def __init__(self, tyyppimäärä, siirtomäärä):
        self.tyyppi = []
        self.siirrot = siirtomäärä
        self.heikkous = []

    def siirron_lasku(self):
        if self.siirrot > 0:
            self.siirrot -= 1


if __name__ == '__main__':
    # a = Vihollinen(3, 7)
    # print(a.tyyppi)
    b = 123
    c = 'aaa'