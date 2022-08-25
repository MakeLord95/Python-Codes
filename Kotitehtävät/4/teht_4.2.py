inch = int(input("Syötä pituus tuumissa: "))

while inch >= 0:
    cm = inch * 2.54
    print(f"{cm:.2f}")
    inch = int(input("Syötä pituus tuumissa: "))
