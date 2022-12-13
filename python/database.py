import mysql.connector


apikey = "cd6c905dd4cd2cdaf0b0f583cb078ec7" #testausta varten voi lisätä tähän apikeyn
salasana = "juurisalis" #testausta varten voi lisätä tähän salasanan
tietokanta = 'flight_game'
käyttäjä = 'root'


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            database=tietokanta,
            user=käyttäjä,
            password=salasana,
            autocommit=True)
        self.apikey=apikey

    def get_connection(self):
        return self.connection
