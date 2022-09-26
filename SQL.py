import mysql.connector

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


class Yhteys:
    def __init__(self, salasana):
        yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password=salasana,
            autocommit=True)
        self.cursor = yhteys.cursor()

    def _exec(self, SQLstring):
        self.cursor.execute(SQLstring.payload)

    def hae(self, SQLstring, monta=False):
        self._exec(SQLstring)
        if monta:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()


class SQLstring:
    payload = ''

    def where(self, *args):
        self.payload += ' WHERE '
        for arg in args:
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
    aa = Select(Airport('ident', 'name'), Country('name')).where('1=1')
    print(aa.payload)
