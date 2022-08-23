leiviska = float(input("Anna leiviskät: "))

naula = float(input("Anna naulat: "))

luoti = float(input("Anna luodit: "))

# print(f"Leiviskät: {leiviska}")
# print(f"Naulat: {naula}")
# print(f"Luodit: {luoti}")

naula2 = (leiviska * 20) + naula
# print(f"Naulat 2 : {naula2}")

luoti2 = (naula2 * 32) + luoti
# print(f"Luodit 2 : {luoti2}")

gramma = (luoti2 * 13.3)
# print(f"Grammaa: {gramma}")

kilogramma = gramma // 1000
gramma2 = gramma % 1000
# print(f"Kilogrammaa: {kilogramma:.0f}")
# print(f"Grammaa: {gramma2:.2f}")

print(f"Massa nykymittojen mukaan: ")
print(f"{kilogramma:.0f} kilogrammaa ja {gramma2:.2f} grammaa.")
