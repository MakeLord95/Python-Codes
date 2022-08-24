value1 = int(input("Syötä ensimmäinen luku: "))
value2 = int(input("Syötä toinen luku: "))

print("Valitse laskutoimitus")
print("1: +")
print("2: -")
print("3: *")
print("4: /")
userinput = input("Valinta: ")

if userinput == '1':
    value3 = value1 + value2
    print(f"Laskun tulos: {value3:.4f}")

if userinput == '2':
    value3 = value1 - value2
    print(f"Laskun tulos: {value3:.4f}")

if userinput == '3':
    value3 = value1 * value2
    print(f"Laskun tulos: {value3:.4f}")

if userinput == '4':
    value3 = value1 / value2
    print(f"Laskun tulos: {value3:.4f}")
