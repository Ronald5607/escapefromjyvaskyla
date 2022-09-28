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

    def draw_line(self, x, y, length):
        if x + length < self.width and y < self.height:
            for i in range(length):
                if self.buffer[x + self.width * y + i] == '|':
                    self.draw_corner(x + i, y)
                else:
                    self.buffer[x + self.width * y + i] = '-'
        else:
            raise ValueError('yli rajojen.')

    def draw_underline(self, x, y, length):
        if x + length < self.width and y < self.height:
            for i in range(length):
                self.buffer[x + self.width * y + i] = '_'
        else:
            raise ValueError('yli rajojen.')

    def draw_corner(self, x, y):
        if x < self.width and y < self.height:
            self.buffer[x + self.width * y] = '+'
        else:
            raise ValueError('yli rajojen.')

    def draw_vertical_line(self, x, y, length):
        if x < self.width and y + length < self.height:
            for i in range(length):
                if self.buffer[x + (self.width * i) + (y * self.width)] == '-':
                    self.draw_corner(x, y + i)
                else:
                    self.buffer[x + (self.width * i) + (y * self.width)] = '|'
        else:
            raise ValueError('yli rajojen.')

    def draw_text(self, x, y, text):
        if x + len(text) < self.width and y < self.height:
            for i in range(len(text)):
                self.buffer[x + self.width * y + i] = text[i]
        else:
            raise ValueError('yli rajojen.')

    def draw_box(self, x, y, width, height):
        if x + width < self.width and y + height < self.height:
            self.draw_line(x, y, width)
            self.draw_line(x, y + height - 1, width)
            self.draw_vertical_line(x, y, height)
            self.draw_vertical_line(x + width - 1, y, height)
        else:
            raise ValueError('yli rajojen.')

    def draw_text_box(self, x, y, *texts):
        i = 0
        max_width = 0
        for text in texts:
            width = len(text) + 4
            height = len(texts) + 2
            if width > max_width:
                max_width = width
            if x + width < self.width and (y + height) < self.height:
                self.draw_text(x + 2, y + 1 + i, text)
            i += 1
        print(max_width)
        self.draw_box(x, y, max_width, height)


if __name__ == '__main__':

    a = Screen()
    a.clear()
    print(a.size, a.width, a.height)
    print(len(a.buffer))
    a.draw_text_box(10,10,'aa', 'bbbbbb', 'c')
    a.flush()
    input('a')
    a.clear()

