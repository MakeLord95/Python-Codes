import json

import flask

app = flask.Flask(__name__)


@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    tulos = test_prime(luku)

    vastaus = {
        "number": luku,
        "isPrime": tulos
    }

    json_data = json.dumps(vastaus, default=lambda o: o.__dict__, indent=4)
    return json_data


def test_prime(luku):
    not_prime = False
    if luku > 1:
        for i in range(2, luku):
            if (luku % i) == 0:
                not_prime = True
                break

        if not_prime:
            print(f"{luku} ei ole alkuluku.")

        else:
            print(f"{luku} on alkuluku.")

    else:
        print(f"{luku} ei ole alkuluku.")

    return not not_prime


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
