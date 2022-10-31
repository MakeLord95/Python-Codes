import mysql.connector


def airport_search(country_code):
    sql = "select type, count(type) from airport where iso_country = '" + country_code + "' group by type order by count(type);"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        print(f"{i[0]} : {i[1]}")


yhteys = mysql.connector.connect(
    host='make-s.duckdns.org',
    port=19915,
    user='lentopeli',
    password='fl1ght_g4m3',
    database='lentopeli',
    autocommit=True
)

iso_country = input("Anna maakoodi: ").upper()
airport_search(iso_country)
