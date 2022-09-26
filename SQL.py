
class Table:
    search = ('*',)

    def __init__(self, *args):
        self.search = ()
        for arg in args:
            if not hasattr(self, arg):
                raise Exception(f'ei ole saraketta {arg}')
            self.search = args


class Airport(Table):
    name = 'airport'
    ident = 'ident'
    type = 'type'
    latitude = 'latitude_deg'
    longitude = 'longitude_deg'
    elevation = 'elevation_ft'
    continent = 'continent'
    country = 'iso_country'


class Country(Table):
    name = 'country'
    country = 'iso_country'


class SQLstring:
    payload = ''

    def SQLfrom(self, *args):
        self.payload += ' FROM '
        for arg in args:
            self.payload += str(arg) + ', '
        self.payload = self.payload.rstrip(', ')
        return self

    def SQLwhere(self, **kwargs):
        self.payload += ' WHERE '
        for arg in kwargs:
            self.payload += str(arg)
        return self


class Select(SQLstring):
    def __init__(self, *args):
        self.payload += 'SELECT '
        frompayload = ' FROM '
        for table in args:
            for column in table.search:
                self.payload += str(table.name + '.' + column) + ', '

            frompayload += str(table.name)
            frompayload += ', '
        self.payload = self.payload.rstrip(', ')
        frompayload = frompayload.rstrip(', ')
        self.payload += frompayload


if __name__ == '__main__':
    aa = Select(Airport('ident', 'name'), Country('name'))
    print(aa.payload)
