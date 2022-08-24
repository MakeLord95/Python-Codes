pituus = int(input("Kuhan pituus centtimetreinä: "))

if pituus < 37:
    print("Kuha on liian pieni!")
    print("Kuha pitää laskea takaisin järveen!")
    mini_pit = 37 - pituus
    print(f"Salitusta pyyntimitasta puuttuu {mini_pit} cm!")

else:
    print("Kuha on tarpeeksi iso.")
    print("Kuhaa ei tarvitse laskea järveen.")
