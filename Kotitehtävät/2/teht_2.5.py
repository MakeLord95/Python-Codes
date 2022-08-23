leiviska = float(input("Anna leiviskät: "))

naula = float(input("Anna naulat: "))

luoti = float(input("Anna luodit: "))

# print(f"Leiviskät: {leiviska}")
# print(f"Naulat: {naula}")
# print(f"Luodit: {luoti}")

naula2 = (leiviska * 20) + naula
# Munnetaan leiviskät nauloiksi ja lisätään päälle käyttäjän syöttämät naulat
# print(f"Naulat 2 : {naula2}")

luoti2 = (naula2 * 32) + luoti
# Muunnetaan naulat luodeiksi ja lisätän päälle käyttäjän syöttämät luodit
# print(f"Luodit 2 : {luoti2}")

gramma = (luoti2 * 13.3)
# Muunnetaan luodit grammoiksi
# print(f"Grammaa: {gramma}")

kilogramma = gramma // 1000
# Jaetaan grammat tuhannella käyttämällä // (Unohtaa kaiken mitä jäisi jäljelle jakolaskusta (esim 23.876 = 23.0))

gramma2 = gramma % 1000
# Jaetaan grammat tuhannella käyttämällä % (Unohtaa kokoluvun kokonaan ja käyttää pelkästään numeroita jotka jäävät
# desimaalin taakse (esim 23.876 = 876))

print(f"Massa nykymittojen mukaan: ")
print(f"{kilogramma:.0f} kilogrammaa ja {gramma2:.2f} grammaa.")
