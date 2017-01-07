#Za zadato ime datoteke funckija vraca sve redove iz datoteke, bez \n
def procitajDatoteku(imeDatoteke):

    file = open("podaci/" + imeDatoteke, "r")
    sviRedovi = file.read().splitlines()
    return sviRedovi