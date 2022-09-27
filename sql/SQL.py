import mysql.connector


class Column:
    def __init__(self, name):
        self.owner = None
        self.name = name

    def __get__(self, instance, owner):
        if instance:
            self.owner = instance
        return self

    def __str__(self):
        if self.owner:
            return self.owner.tablename + '.' + self.name
        else:
            return self.name

    def __add__(self, other):
        return self.name + other

    def __radd__(self, other):
        return other + self.name

    def __lt__(self, other):
        if other == Column:
            return str(self) + '<' + str(other)
        else:
            return str(self) + '<' + "'" + str(other) + "'"

    def __eq__(self, other):
        if other == Column:
            return str(self) + '=' + str(other)
        else:
            return str(self) + '=' + "'" + str(other) + "'"


class Table:
    search = (Column('*'),)

    def __init__(self, *args):
        self.search = ()
        for arg in args:
            if not hasattr(self, arg):
                raise Exception(f'ei ole saraketta {arg}')
        self.search = args


class Airport(Table):
    tablename = 'airport'
    name = Column('name')
    ident = Column('ident')
    type = Column('type')
    latitude = Column('latitude_deg')
    longitude = Column('longitude_deg')
    elevation = Column('elevation_ft')
    continent = Column('continent')
    country = Column('iso_country')


class Country(Table):
    tablename = 'country'
    name = Column('name')
    country = Column('iso_country')


class Yhteys:
    def __init__(self, salasana):
        self.yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password=salasana,
            autocommit=True)
        self.cursor = self.yhteys.cursor()

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

    def where(self, arg):
        self.payload += ' WHERE '
        self.payload += str(arg)
        return self

    def AND(self, arg):
        self.payload += ' AND '
        self.payload += str(arg)
        return self

    def limit(self, limit):
        self.payload += ' LIMIT ' + str(limit)
        return self


class Select(SQLstring):
    def __init__(self, *args):
        self.payload += 'SELECT '
        frompayload = ' FROM '
        for table in args:
            for column in table.search:
                self.payload += str(table.tablename) + '.' + str(column) + ', '

            frompayload += str(table.tablename)
            frompayload += ', '
        self.payload = self.payload.rstrip(', ')
        frompayload = frompayload.rstrip(', ')
        self.payload += frompayload


if __name__ == '__main__':
    sql = Yhteys('roni')
    airport = Airport('ident', 'name')
    country = Country('name')
    aa = (Select(airport, country)
          .where(country.country == airport.country)
          .AND(country.name == 'Finland')
          .limit(10))
    print(aa.payload)
    print(sql.hae(aa, monta=False))

