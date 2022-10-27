import json
import flask
import mysql.connector

app = flask.Flask(__name__)

yhteys = mysql.connector.connect(
    host='make-s.duckdns.org',
    port=3306,
    user='lentopeli',
    password='fl1ght_g4m3',
    database='lentopeli',
    autocommit=True
)


def kursori_func(sql_command):
    kursori = yhteys.cursor()

    kursori.execute(sql_command)

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


@app.route('/kentta/')
def kentta():
    args = flask.request.args
    icao = str(args.get("")).upper()

    ident = icao.upper()
    nimi = get_airport_name(icao)[0][0]
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
