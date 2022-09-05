import mysql.connector
from collections import Counter


def airport_search(country_code):
    # sql = "select name, municipality from airport where gps_code = '\"" + gps_code + "\"';"
    sql = "select type from airport where iso_country = '\"" + country_code + "\"';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    x = Counter(tulos)

    print(x)


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

# iso_country = input("Anna maakoodi: ").upper()
iso_country = "FI"
airport_search(iso_country)
