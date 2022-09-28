from random import randint
class Vihollinen:
    tyypit = {'iceman': 'kuuma',
              'tuliukko': 'kylmä',
              'pieni':'large_airport',
              'iso': 'small_airport',
              'pitka': 'elevation_ft',
              'lyhyt': 'elevation_ft'}

    def __init__(self, tyyppimäärä, siirtomäärä):
        self.tyyppi = [self.tyypit[randint(0,6)] for x in range(tyyppimäärä)]
        self.siirrot = siirtomäärä

    # tulostaa heikkouden tyypin mukaan
    @property
    def heikkous(self):
        ...


if __name__ == '__main__':
    a = Vihollinen(3, 7)
    print(a.tyyppi)
    b = 123
    c = 'aaa'
    print(type(b), type(c))
    if type(b) == type(c):
        print('aa')