import mysql.connector


def airport_search(gps_code):
    sql = "select name, municipality from airport where gps_code = '\"" + gps_code + "\"';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

ICAO_Code = input("Anna ICAO koodi: ").upper()
airport_search(ICAO_Code)
