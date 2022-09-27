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
    def emptyline():
        print('/n')


if __name__ == '__main__':

    print(os.name)
    a = Screen()
    a.get_size()
    a.clear()
    print(a.size)
    input('c')
    a.clear()
    a.get_size()
    print(a.size)
    input('b')

