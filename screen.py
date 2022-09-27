import shutil
import os


class Screen:
    # hoitaa terminaalille tulostamisen.
    # __init__() kutsutaan kun luodaan objekti Screen.
    def __init__(self):
        self._size = shutil.get_terminal_size()
        self.width, self.height = self._size

# @property dekoraattori tarkoittaa että metodin size voi kutsua ilman sulkuja "Screen.size"
    @property
    def size(self):
        return self._size

# hakee terminaalin koon.
    def get_size(self):
        self._size = shutil.get_terminal_size()
        self.width, self.height = self._size

# @staticmethod ei tarvitse objektia parametrinä, voi kutsua ilman objektia. metodi pyyhkii terminaali ruudun.
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

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

    def line(self):
        print('-' * self.width)

    def uline(self):
        print('_' * self.width)


if __name__ == '__main__':

    print(os.name)
    a = Screen()
    a.clear()
    print(a.size)
    a.line()
    a.whitespace(5)
    input('c')
    a.clear()
    a.get_size()
    a.uline()
    print(a.size)
    input('b')

