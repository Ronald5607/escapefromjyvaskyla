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
            return self.owner.name + '.' + self.name
        else:
            return self.name

    def __add__(self, other):
        return self.name + other

    def __radd__(self, other):
        return other + self.name

    def __lt__(self, other):
        return self.name + '<' + other

    def __eq__(self, other):
        return self.name + '=' + other


class Table:
    search = (Column('*'),)

    def __init__(self, *args):
        self.search = ()
        temp = []
        for arg in args:
            if not hasattr(self, arg):
                raise Exception(f'ei ole saraketta {arg}')
            else:
                temp.append(Column(arg))
            self.search = tuple(temp)




class Airport(Table):
    name = Column('airport')
    ident = Column('ident')
    type = Column('type')
    latitude = Column('latitude_deg')
    longitude = Column('longitude_deg')
    elevation = Column('elevation_ft')
    continent = Column('continent')
    country = Column('iso_country')


class Country(Table):
    name = Column('country')
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

    def where(self, *args):
        self.payload += ' WHERE '
        for arg in args:
            self.payload += "'" + str(arg) + "'"
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
                self.payload += str(table.name) + '.' + str(column) + ', '

            frompayload += str(table.name)
            frompayload += ', '
        self.payload = self.payload.rstrip(', ')
        frompayload = frompayload.rstrip(', ')
        self.payload += frompayload


if __name__ == '__main__':
    # sql = Yhteys('roni')
    airport = Airport('ident', 'name')
    country = Country('name')
    print(country.name)
    aa = (Select(airport, country)
            .where(country.country == airport.country)
            .limit(10))
    # print(sql.hae(aa, monta=True))
    print(aa.payload)
