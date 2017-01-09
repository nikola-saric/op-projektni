test_mode = False

#Za zadato ime datoteke funckija vraca sve redove iz datoteke, bez \n
def procitaj_datoteku(ime_datoteke):
    file = open(_vrati_folder() + ime_datoteke, "r")
    return file.read().splitlines()

def upisi_u_datoteku(imeDatoteke, staSeUpisuje):
    karteFile = open(_vrati_folder() + imeDatoteke, "a")
    karteFile.write(staSeUpisuje)
    karteFile.close()

def _vrati_folder():
    if test_mode: return "test_podaci/"
    return "podaci/"