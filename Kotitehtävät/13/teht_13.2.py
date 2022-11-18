import json

import flask
import mysql.connector

app = flask.Flask(__name__)


def mariadb_connect():
    yhteys = mysql.connector.connect(
        host='make-s.duckdns.org',
        port=19915,
        database='lentopeli',
        user='lentopeli',
        password='fl1ght_g4m3',
        autocommit=True
    )

    return yhteys


def kursori_func(sql_komento):
    yhteys = mariadb_connect()

    kursori = yhteys.cursor()

    kursori.execute(sql_komento)

    tulos = kursori.fetchall()

    return tulos


def get_airport_name(ident):
    sql_get_airport_name = f"select name from airport where ident = '{ident}';"
    sql_result = kursori_func(sql_get_airport_name)
    return sql_result


def get_airport_municipality(ident):
    sql_get_airport_municipality = f"select municipality from airport where ident = '{ident}';"
    sql_result = kursori_func(sql_get_airport_municipality)
    return sql_result


@app.route('/kentta/<string:airport>')
def kentta(airport):

    ident = airport.upper()
    nimi = get_airport_name(ident)[0][0]
    municipality = get_airport_municipality(ident)[0][0]

    vastaus = {
        "ICAO": ident,
        "Name": nimi,
        "Municipality": municipality
    }

    json_data = json.dumps(vastaus, default=lambda o: o.__dict__, indent=4)
    return json_data


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
