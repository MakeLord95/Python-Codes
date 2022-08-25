import math

nbr_str = input("Syötä luku: ")
nbr_big = -math.inf
nbr_smol = math.inf

while nbr_str != '':

    nbr = int(nbr_str)

    if nbr > nbr_big:
        nbr_big = nbr

    if nbr < nbr_smol:
        nbr_smol = nbr

    nbr_str = input("Syötä luku: ")
if nbr_big == -math.inf or nbr_smol == math.inf:
    print("Et syöttänyt arvoja!")

else:
    print(f"Suurin syöttämäsi luku: {nbr_big}")
    print(f"Pienin syöttämäsi luku: {nbr_smol}")
