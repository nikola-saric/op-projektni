#Za zadato ime datoteke funckija vraca sve redove iz datoteke, bez \n
def procitaj_datoteku(ime_datoteke):
    file = open(ime_datoteke, "r")
    return file.read().splitlines()

def upisi_u_datoteku(imeDatoteke, staSeUpisuje):
    karteFile = open(imeDatoteke, "a")
    karteFile.write(staSeUpisuje)
    karteFile.close()

