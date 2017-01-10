# lista karata koje prodavac rezervise i koje se stampaju.
import datoteka


class Karta:
    def __init__(self, nazivLeta, imePutnika, prezimePutnika, drzavPutnika, brojPasosaPutnika, datumLeta):
        self.nazivLeta = nazivLeta
        self.imePutnika = imePutnika
        self.prezimePutnika = prezimePutnika
        self.drzavPutnika = drzavPutnika
        self.brojPasosaPutnika = brojPasosaPutnika
        self.datumLeta = datumLeta

    def print_karte(self):
        print("Let: ", self.nazivLeta)
        print("Ime putnika: ", self.imePutnika)
        print("Prezime putnika: ", self.prezimePutnika)
        print("Drzavljanstvo: ", self.drzavPutnika)
        print("Broj pasosa: ", self.brojPasosaPutnika)
        print("Sediste: jos nema, ali bice! ")
        print("Datum leta: ", self.datumLeta)
        print("============\n")

    def upisi_karte(self):
        kartaStr = self.nazivLeta + "|" + self.imePutnika + "|" + self.prezimePutnika + "|" + self.drzavPutnika + "|" + self.brojPasosaPutnika + "|" + self.datumLeta + "\n"
        datoteka.upisi_u_datoteku("karte.txt", kartaStr)


class KartaServis():
    def obrisi_kartu(nazivLetaKarta, brojPasosaKarta, datumKarta):
        nepostojecaKarta = True
        karteRedovi = datoteka.procitaj_datoteku("karte.txt")
        for kartaRed in karteRedovi:
            karta = kartaRed.split("|")
            if (karta[0] == nazivLetaKarta) and (karta[4] == brojPasosaKarta) and (karta[5] == datumKarta):
                karteRedovi.remove(kartaRed)
                nepostojecaKarta = False

        if nepostojecaKarta == True:
            print("Ne postoji karta sa tim podacima.")
        else:
            print("Karta je obrisana.")

        karteFile = open("podaci/karte.txt", "w")
        for kartaRed in karteRedovi:
            karteFile.write("%s\n" % kartaRed)
        karteFile.close()

    def izmeni_kartu(nazivLetaKarta, brojPasosaKarta, datumKarta):

        nepostojecaKarta = True
        staroIme = ""
        staroPrezime = ""
        staroDrzavljanstvo = ""
        karteRedovi = datoteka.procitaj_datoteku("karte.txt")
        for kartaRed in karteRedovi:
            karta = kartaRed.split("|")
            if (karta[0] == nazivLetaKarta) and (karta[4] == brojPasosaKarta) and (karta[5] == datumKarta):
                staroIme = karta[1]
                staroPrezime = karta[2]
                staroDrzavljanstvo = karta[3]
                karteRedovi.remove(kartaRed)
                nepostojecaKarta = False

            if nepostojecaKarta == True:
                print("Ne postoji karta sa tim podacima.")
            else:
                print("Karta je izmenjena.")
            karteFile = open("podaci/karte.txt", "w")
            for kartaRed in karteRedovi:
                karteFile.write("%s\n" % (kartaRed))
            karteFile.close()
        return staroIme, staroPrezime, staroDrzavljanstvo
