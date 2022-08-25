vuosi = int(input("Syötä vuosiluku: "))
if vuosi % 4 == 0:
    if vuosi % 100 == 0 and vuosi % 400 == 0:
        print("Karkausvuosi")

    elif vuosi % 4 == 0 and vuosi % 100 != 0:
        print("Karkausvuosi!")

    else:
        print("Ei ole karkausvuosi!")

else:
    print("Ei ole karkausvuosi!")
