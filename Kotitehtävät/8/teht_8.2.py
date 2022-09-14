import mysql.connector


def airport_search(country_code):
    sql = "select type, count(type) from airport where iso_country = '" + country_code + "' group by type order by count(type) asc;"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for i in tulos:
        print(f"{i[0]} : {i[1]}")


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

iso_country = input("Anna maakoodi: ").upper()
airport_search(iso_country)
