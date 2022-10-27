import mysql.connector


def airport_search(gps_code):
    sql = "select name, municipality from airport where gps_code = '" + gps_code + "';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


yhteys = mysql.connector.connect(
    host='make-s.duckdns.org',
    port=19915,
    user='lentopeli',
    password='fl1ght_g4m3',
    database='lentopeli',
    autocommit=True
)

ICAO_Code = input("Anna ICAO koodi: ").upper()
airport = airport_search(ICAO_Code)

if not airport:
    print("Et syöttänyt kunnollista ICAO-koodia!")

else:
    for i in airport:
        print(f"{i[0]}: {i[1]}")
