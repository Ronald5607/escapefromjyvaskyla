import shutil
import os

# 2d pisteen sijainti 1d listassa on (x + y * width)


class Screen:
    # hoitaa terminaalille tulostamisen.
    # __init__() kutsutaan kun luodaan objekti Screen.
    def __init__(self):
        self._size = shutil.get_terminal_size()
        self.width, self.height = self._size
        self.buffer = [' ' for i in range(self.width * self.height)]

# @property dekoraattori tarkoittaa että metodin size voi kutsua ilman sulkuja "Screen.size"
    @property
    def size(self):
        return self._size

# hakee terminaalin koon.
    def get_size(self):
        self._size = shutil.get_terminal_size()
        self.width, self.height = self._size

    def flush(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.buffer[i * self.width + j], end='')
            print('\n', end='')

# metodi pyyhkii terminaali ruudun.
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.buffer = [' ' for i in range(self.width * self.height)]

    def set_prompt(self):
        ...

    def drawline(self, x, y, length):
        if x + length < self.width and y < self.height:
            for i in range(length):
                self.buffer[x + self.width * y + i] = '-'
        else:
            raise ValueError('yli rajojen.')

    def drawuline(self, x, y, length):
        for i in range(length):
            self.buffer[x + self.width * y + i] = '_'


if __name__ == '__main__':

    a = Screen()
    a.clear()
    print(a.size, a.width, a.height)
    a.drawuline(10, 10, 100)
    a.flush()
    input('a')
    a.clear()
    a.drawline(5, 20, 20)
    a.get_size()
    a.flush()
    input('b')

