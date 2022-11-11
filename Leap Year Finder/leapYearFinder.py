vuosi = 0
karkausvuodet = []

while vuosi <= 2400:
    if vuosi % 4 == 0 and vuosi != 0:
        if vuosi % 100 == 0 and vuosi % 400 == 0:
            print(vuosi)
            karkausvuodet.append(vuosi)

        elif vuosi % 4 == 0 and vuosi % 100 != 0:
            print(vuosi)
            karkausvuodet.append(vuosi)
    vuosi = vuosi + 1

with open("leaps.txt", "w") as outfile:
    for i in karkausvuodet:
        outfile.write(f"{str(i)}\n")

