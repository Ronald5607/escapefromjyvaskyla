from geopy import distance
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password="R00tS4l4s4n4",
         autocommit=True
        )

icao1=input("Anna ensimmäisen lentoaseman ICAO-koodi: ")
sql=f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{icao1}'"
kursori=yhteys.cursor()
kursori.execute(sql)
asema1=kursori.fetchone()
latitude=str(asema1[0])
longitude=str(asema1[1])
print(longitude)
print(latitude)
sql=("SELECT ident, name, longitude_deg, latitude_deg, SQRT(POWER((latitude_deg-"+latitude+"),2)+POWER(longitude_deg-"+longitude+",2)) FROM airport WHERE ident!='"+icao1+"' and iso_country='FI'")
kursori.execute(sql)
asema2=kursori.fetchall()
for i in asema2:
    print(i)
