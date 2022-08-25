OHJELMA KESKEN!
EI OLE VIELÄ VALMIS!!!

nbr = input("Syötä luku: ")
nbr_big = nbr
nbr_smol = nbr
while nbr != '':
    if nbr_big < nbr:
        nbr_big = nbr

    if nbr_smol > nbr and nbr_smol < nbr_big:
        nbr_smol = nbr

    nbr = input("Syötä luku: ")

print(nbr_big)
print(nbr_smol)
