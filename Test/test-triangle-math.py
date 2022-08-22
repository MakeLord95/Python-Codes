# Tämä ohjelma laskee kolmion pinta-alan
# Kun käyttäjä syöttää kannan sekä korkeuden

kanta = float(input("Anna kolmion kanta: "))
print(kanta)

korkeus = float(input("Anna kolmion korkeus: "))
print(korkeus)

ala = (kanta * korkeus) / 2

print(str(kanta) + " * " + str(korkeus) + " / 2.0  = " + str(ala))

print("Kolmion pinta-ala: " + str(ala))
