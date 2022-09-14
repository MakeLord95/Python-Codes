import mysql.connector
from geopy import distance


def airport_search(icao_code):
    sql = "select latitude_deg, longitude_deg from airport where ident = '\"" + icao_code + "\"';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

if True:
    ICAO = input("Anna ensimmäisen lentokentän ICAO koodi: ").upper()
    airport_1 = airport_search(ICAO)

    ICAO_2 = input("Anna toisen lentokentän ICAO koodi: ").upper()
    airport_2 = airport_search(ICAO_2)

    if not airport_1 or not airport_2:
        print("Et syöttänyt kunnollista ICAO-koodia!")

    else:
        print(f"Kenttien etäisyys toisistaan: {distance.distance(airport_1, airport_2).km:.2f}km")
