import os


class Screen:
    # hoitaa terminaalille tulostamisen.
    def __init__(self):
        self._size = 0

    @property
    def size(self):
        return self._size

    def get_size(self):
        self._size = os.get_terminal_size()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def set_prompt(self):
        ...



if __name__ == '__main__':
    print('a')
    a = Screen()
    a.set_prompt()
    input('a')
    print('b')
    input('b')

