# lista karata koje prodavac rezervise i koje se stampaju.
class Karta:
    def __init__(self, nazivLeta, imePutnika, prezimePutnika, drzavPutnika, brojPasosaPutnika):
        self.nazivLeta = nazivLeta
        self.imePutnika = imePutnika
        self.prezimePutnika = prezimePutnika
        self.drzavPutnika = drzavPutnika
        self.brojPasosaPutnika = brojPasosaPutnika

    def proveraVremena(nazivLeta):
        letoviFile = open("letovi.txt", "r")
        letoviRF = letoviFile.readlines()
        lenLetovi = len(letoviRF)
        for i in range(lenLetovi):
            jedanLet = letoviRF[i]
            noviLet = jedanLet.split("|")
            if nazivLeta == noviLet[0]:
                polaziste = noviLet[1]
                vremePoletanja = noviLet[3]
                return polaziste, vremePoletanja

    def mesta(self, nazivLeta):
        letoviFile = open("letovi.txt", "r")
        letoviRF = letoviFile.readlines()
        lenLetovi = len(letoviRF)
        for i in range(lenLetovi):
            jedanLet = letoviRF[i]
            noviLet = jedanLet.split("|")
            if nazivLeta == noviLet[0]:
                sedista = noviLet[7]
                listaSedista = sedista.split("/")
                brReda = eval(listaSedista[0])
                brSedista = eval(listaSedista[1])
                brojMestaUAvionu = brReda * brSedista
                return brojMestaUAvionu


    def printKarte(self):

        print("Let: ", self.nazivLeta)
        print("Ime putnika: ", self.imePutnika)
        print("Prezime putnika: ", self.prezimePutnika)
        print("Drzavljanstvo: ", self.drzavPutnika)
        print("Broj pasosa: ", self.brojPasosaPutnika)
        print("Sediste: ", self.mesta(self.nazivLeta))
        print("============\n")
