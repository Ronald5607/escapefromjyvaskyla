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
komento=1
recent=[]
while 0<komento<6:
    sql=f"SELECT latitude_deg, longitude_deg, name, ident FROM airport WHERE ident='{icao1}'"
    kursori=yhteys.cursor()
    kursori.execute(sql)
    asema1=kursori.fetchone()
    latitude=str(asema1[0])
    longitude=str(asema1[1])
    recent.append(asema1[3])
    print(asema1[2])
    print(longitude)
    print(latitude)
    coordinates_1=(latitude,longitude)
    sql=("SELECT ident, name, latitude_deg, longitude_deg FROM airport WHERE iso_country='FI' and ident!='"+icao1+"'")
    kursori.execute(sql)
    tulos=kursori.fetchall()
    etaisyydet=[]
    asemat=[]
    for i in tulos:
        if i[0] not in recent:
            coordinates_2=(i[2], i[3])
            etaisyys = (distance.distance(coordinates_1, coordinates_2).km)
            #print(f"Lentoasemien välinen etäisyys on {etaisyys:.2f} kilometriä")
            etaisyydet.append(float(etaisyys))
            asemat.append((i[0],i[1],i[2],i[3], etaisyys,f"Lentoasemien välinen etäisyys on {etaisyys:.2f} kilometriä"))
    #for rivi in etaisyydet:
            #print(rivi)

    #print(etaisyydet)
    etaisyydet.sort()
    numero=1
    valittavat=[]
    for asema in asemat:
        if asema[4] in etaisyydet[0:5]:
            print(f"{numero}: {asema}")
            valittavat.append(asema)
            numero+=1
    komento=int(input("valitse aseman numero: "))
    icao1=valittavat[komento-1][0]
    print(recent)
    if len(recent)==10:
        recent.remove(recent[0])
