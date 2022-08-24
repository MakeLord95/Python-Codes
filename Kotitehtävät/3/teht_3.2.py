luokka = input("Hyttiluokka: ")

if luokka in ('LUX', 'A', 'B', 'C'):
    if luokka == 'LUX':
        print("LUX on parvekkeellinen hytti yläkannella.")

    elif luokka == 'A':
        print("A on ikkunallinen hytti autokannen yläpuolella.")

    elif luokka == 'B':
        print("B on ikkunaton hytti autokannen yläpuolella.")

    else:
        print("C on ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka")
