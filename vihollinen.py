from random import randint
class Vihollinen:
    tyypit = ('iceman', 'tuliukko', 'pieni', 'iso', 'vihaaja', 'pitka', 'lyhyt')

    def __init__(self, tyyppimäärä, siirtomäärä):
        self.tyyppi = [self.tyypit[randint(0,6)] for x in range(tyyppimäärä)]
        self.siirrot = siirtomäärä



if __name__ == '__main__':
    a = Vihollinen(3, 7)
    print(a.tyyppi)