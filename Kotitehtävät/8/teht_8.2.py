import mysql.connector


def airport_search(country_code):
    # sql = "select name, municipality from airport where gps_code = '\"" + gps_code + "\"';"
    sql = "select type from airport where iso_country = '\"" + country_code + "\"' order by type asc;"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for x in tulos:
        tulos.count(tulos[x])



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

# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI)
# ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on
# 15 kappaletta jne.
