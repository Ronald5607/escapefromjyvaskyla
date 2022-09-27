import shutil
import os


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
            print('\n', end='')
            for j in range(self.width):
                print(self.buffer[i + j], end='')

# metodi pyyhkii terminaali ruudun.
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.buffer = ['1' for i in range(self.width * self.height)]

    def set_prompt(self):
        ...

    @staticmethod
    def emptyline(n=1):
        print('\n' * n, end='')

    def whitespace(self, n):
        if n < self.width:
            print(' ' * n, end='')
        else:
            raise ValueError('liian monta tyhjää merkkiä (Screen.whitespace())')

    def _line(self):
        print('-' * self.width)

    def drawline(self, x, y, length):
        if x + length < self.width and y < self.height:
            for i in range(length):
                self.buffer[x + self.width * y + i] = '-'
        else:
            raise ValueError('yli rajojen.')

    def _uline(self):
        print('_' * self.width)

    def drawuline(self, x, y, length):
        for i in range(length):
            self.buffer[x + self.width * y + i] = '_'


if __name__ == '__main__':

    a = Screen()
    a.clear()
    a.drawuline(10, 10, 10)
    a.flush()
    input('a')
    a.clear()
    a.get_size()
    input('b')

