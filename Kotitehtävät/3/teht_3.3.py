sukupuoli = input("Syötä sukupuolesi (m / n): ")

if sukupuoli in ('m', 'n'):

    Hb = int(input("Syötä hemoglobiiniarvosi (g/l): "))

    if sukupuoli == 'm':
        if 134 <= Hb <= 195:
            print("Hemoglobiiniarvo on normaali!")

        elif Hb < 134:
            print("Hemoglobiiniarvo on alhainen!")

        elif Hb > 195:
            print("Hemoglobiiniarvo on korkea!")

        else:
            print("Virhe!")

    else:
        if 117 <= Hb <= 175:
            print("Hemoglobiiniarvo on normaali!")

        elif Hb < 117:
            print("Hemoglobiiniarvo on alhainen!")

        elif Hb > 175:
            print("Hemoglobiiniarvo on korkea!")

        else:
            print("Virhe!")

else:
    print("Et syöttänyt sukupuolta!")
