# OHJELMA KESKEN!
# EI OLE VIELÄ VALMIS!!!

nbr = input("Syötä luku: ")
nbr_big = nbr
nbr_smol = nbr

while True:
    if nbr != '':
        if nbr > nbr_big:
            nbr_big = nbr

        if nbr < nbr_smol:
            nbr_smol = nbr

        nbr = None
        nbr = input("Syötä luku: ")
    else:
        print(f"Big: {nbr_big}")
        print(f"Smol: {nbr_smol}")
        break
