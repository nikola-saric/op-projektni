# lista karata koje prodavac rezervise i koje se stampaju.
import datoteka
import datetime


class Karta:
    def __init__(self, nazivLeta, imePutnika, prezimePutnika, drzavPutnika, brojPasosaPutnika, datumLeta, sediste,
                 imeProdavca, datumIzdavanja, cena):
        self.nazivLeta = nazivLeta
        self.imePutnika = imePutnika
        self.prezimePutnika = prezimePutnika
        self.drzavPutnika = drzavPutnika
        self.brojPasosaPutnika = brojPasosaPutnika
        self.datumLeta = datumLeta
        self.sediste = sediste
        self.imeProdavca = imeProdavca
        self.datumIzdavanja = datumIzdavanja
        self.cena = cena

    def print_karte(self):
        print("Let: ", self.nazivLeta)
        print("Ime putnika: ", self.imePutnika)
        print("Prezime putnika: ", self.prezimePutnika)
        print("Drzavljanstvo: ", self.drzavPutnika)
        print("Broj pasosa: ", self.brojPasosaPutnika)
        print("Datum leta: ", self.datumLeta)
        print("Vase sediste je: ", self.sediste)
        print("Ime prodavca: ", self.imeProdavca)
        print("Datum izdavanja: ", self.datumIzdavanja)
        print("Cena karte: ", self.cena)
        print("============\n")

    def vrati_naziv_leta(self):
        return self.nazivLeta

    def upisi_kartu(self):
        kartaStr = self.nazivLeta + "|" + self.imePutnika + "|" + self.prezimePutnika + "|" + self.drzavPutnika + "|" + \
                   self.brojPasosaPutnika + "|" + self.datumLeta + "|" + self.sediste + "|" + self.imeProdavca + "|" + \
                   self.datumIzdavanja + "|" + self.cena + "\n"

        datoteka.upisi_u_datoteku("karte.txt", kartaStr)


class KartaServis:
    def obrisi_kartu(self, nazivLetaKarta, brojPasosaKarta, datumKarta):
        nepostojecaKarta = True
        karteRedovi = datoteka.procitaj_datoteku("karte.txt")
        for kartaRed in karteRedovi:
            karta = kartaRed.split("|")
            if (karta[0] == nazivLetaKarta) and (karta[4] == brojPasosaKarta) and (karta[5] == datumKarta):
                karteRedovi.remove(kartaRed)
                nepostojecaKarta = False

        karteFile = open("podaci/karte.txt", "w")
        for kartaRed in karteRedovi:
            karteFile.write("%s\n" % kartaRed)
        karteFile.close()
        return nepostojecaKarta

    def izmeni_kartu(self, nazivLetaKarta, brojPasosaKarta, datumKarta):

        KARTA_NE_POSTOJI = 1
        KARTA_POSTOJI = 2
        staroIme = ""
        staroPrezime = ""
        staroDrzavljanstvo = ""
        staroImeProdavca = ""
        stariDatumIzdavanja = ""
        staraCena = ""
        karteRedovi = datoteka.procitaj_datoteku("karte.txt")
        for kartaRed in karteRedovi:
            karta = kartaRed.split("|")
            if (karta[0] == nazivLetaKarta) and (karta[4] == brojPasosaKarta) and (karta[5] == datumKarta):
                staroIme = karta[1]
                staroPrezime = karta[2]
                staroDrzavljanstvo = karta[3]
                staroImeProdavca = karta[7]
                stariDatumIzdavanja = karta[8]
                staraCena = karta[9]
                karteRedovi.remove(kartaRed)
                nepostojecaKarta = KARTA_POSTOJI

                karteFile = open("podaci/karte.txt", "w")
                for kartaRed in karteRedovi:
                    karteFile.write("%s\n" % kartaRed)
                karteFile.close()
                return staroIme, staroPrezime, staroDrzavljanstvo, staroImeProdavca, stariDatumIzdavanja, staraCena, nepostojecaKarta

        return staroIme, staroPrezime, staroDrzavljanstvo, staroImeProdavca, stariDatumIzdavanja, staraCena, KARTA_NE_POSTOJI

    def zauzeta_sedista(self, nazivLeta, datumLeta):
        zauzetaMesta = []
        procitajKarte = datoteka.procitaj_datoteku("karte.txt")
        for karta in procitajKarte:
            red = karta.split("|")
            if (nazivLeta == red[0]) and (datumLeta == red[5]):
                zauzetaMesta.append(red[6])

        return zauzetaMesta

    def prikazi_slobodna_sedista(self, nazivLeta, datumLeta):

        abc = [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]
        brojRedova = 0
        brojKolona = 0
        zauzetaMesta = self.zauzeta_sedista(nazivLeta, datumLeta)
        redoviKolone = datoteka.procitaj_datoteku("letovi.txt")
        for redoviKoloneLista in redoviKolone:
            red = redoviKoloneLista.split("|")
            if red[0] == nazivLeta:
                kolRed = red[7].split("/")
                brojRedova = eval(kolRed[0])
                brojKolona = eval(kolRed[1])
        for i in range(brojRedova):
            tacanBrojReda = i + 1
            for j in range(brojKolona):
                slobodnoSediste = str(tacanBrojReda) + abc[j]
                if slobodnoSediste in zauzetaMesta:
                    slobodnoSediste = "X"
                print("|" + slobodnoSediste + "|", end=" ")
            print()

    def prodate_karte_za_izabrani_dan_prodaje_ili_polaska(self, izabraniDan, izabranaOpcija):
        DAN_PRODAJE = 1
        DAN_POLASKA = 2
        indexPolja = -1
        if izabranaOpcija == DAN_PRODAJE:
            indexPolja = 8
        elif izabranaOpcija == DAN_POLASKA:
            indexPolja = 5

        pronadjeneKarte = []

        karteRedovi = datoteka.procitaj_datoteku("karte.txt")
        for karta in karteRedovi:
            kartaRed = karta.split("|")
            if izabraniDan == kartaRed[indexPolja]:
                pronadjeneKarte.append(karta)

        return pronadjeneKarte

    def prodate_karte_za_izabrani_dan_prodaje_i_izabranog_prodavca(self, izabraniDan, izabraniProdavac):
        DAN_PRODAJE = 8
        PRODAVAC = 7

        pronadjeneKarte = []

        karteRedovi = datoteka.procitaj_datoteku("karte.txt")
        for karta in karteRedovi:
            kartaRed = karta.split("|")
            if (izabraniDan == kartaRed[DAN_PRODAJE]) and (izabraniProdavac == kartaRed[PRODAVAC]):
                pronadjeneKarte.append(karta)
        return pronadjeneKarte

    def ukupan_broj_prodatih_karata_i_cena_za_izabrani_dan_prodaje_i_polaska(self, izabraniDan, izabranaOpcija):
        DAN_PRODAJE = 4
        DAN_POLASKA = 5
        indexPolja = -1
        ukupnaCena = 0
        brojKarata = 0
        if izabranaOpcija == DAN_PRODAJE:
            indexPolja = 8
        elif izabranaOpcija == DAN_POLASKA:
            indexPolja = 5

        karteRedovi = datoteka.procitaj_datoteku("karte.txt")
        for karta in karteRedovi:
            kartaRed = karta.split("|")
            if izabraniDan == kartaRed[indexPolja]:
                brojKarata += 1
                cenaKarte = eval(kartaRed[9])
                ukupnaCena = ukupnaCena + cenaKarte

        return brojKarata, ukupnaCena

    def ukupan_broj_prodatih_karata_i_cena_za_izabrani_dan_prodaje_i_prodavca(self, izabraniDan, izabraniProdavac):
        DAN_PRODAJE = 8
        PRODAVAC = 7
        ukupnaCena = 0
        brojKarata = 0

        karteRedovi = datoteka.procitaj_datoteku("karte.txt")
        for karta in karteRedovi:
            kartaRed = karta.split("|")
            if (izabraniDan == kartaRed[DAN_PRODAJE]) and (izabraniProdavac == kartaRed[PRODAVAC]):
                brojKarata += 1
                cenaKarte = eval(kartaRed[9])
                ukupnaCena = ukupnaCena + cenaKarte

        return brojKarata, ukupnaCena

    def ukupan_broj_prodatih_karat_i_cena_po_prodavcu_poslednjih_30_dana(self, izabraniProdavac):
        PRODAVAC = 7
        ukupnaCena = 0
        brojKarata = 0
        danasnjiDatum = datetime.date.today()

        karteRedovi = datoteka.procitaj_datoteku("karte.txt")
        for karta in karteRedovi:
            kartaRed = karta.split("|")
            datumProdaje = kartaRed[8]
            intDatumProdajeLista = datumProdaje.split("-")
            godina = int(intDatumProdajeLista[0])
            mesec = int(intDatumProdajeLista[1])
            dan = int(intDatumProdajeLista[2])
            intDatumProdaje = datetime.date(godina, mesec, dan)
            datum = danasnjiDatum - intDatumProdaje
            datumDays = datum.days
            if (izabraniProdavac == kartaRed[PRODAVAC]) and (datumDays <= 30):
                brojKarata += 1
                cenaKarte = eval(kartaRed[9])
                ukupnaCena = ukupnaCena + cenaKarte

        return brojKarata, ukupnaCena

    def prikazi_karte(self, pronadjeneKarte):

        for pronadjenaKarta in pronadjeneKarte:
            kartaLista = pronadjenaKarta.split("|")
            karta = Karta(kartaLista[0], kartaLista[1], kartaLista[2], kartaLista[3], kartaLista[4], kartaLista[5],
                          kartaLista[6], kartaLista[7], kartaLista[8], kartaLista[9])
            Karta.print_karte(karta)

    def cena_karte(self, nazivLeta):
        cena = ""
        letRedovi = datoteka.procitaj_datoteku("letovi.txt")
        for let in letRedovi:
            letRed = let.split("|")
            if letRed[0] == nazivLeta:
                cena = letRed[8]
        return cena

    @staticmethod
    def dan_u_nedelji(datumLeta):
        # dani u nedelji
        PONEDELJAK = 0
        UTORAK = 1
        SREDA = 2
        CETVRTAK = 3
        PETAK = 4
        SUBOTA = 5
        NEDELJA = 6
        danUNedelji = ""
        danUNedeljiInt = 0
        try:
            datumLetaLista = datumLeta.split("/")
            godina = int(datumLetaLista[0])
            mesec = int(datumLetaLista[1])
            dan = int(datumLetaLista[2])
            danUNedeljiInt = datetime.date(godina, mesec, dan).weekday()
        except IndexError:
            print("Uneli ste nepravilne informacije!")
            greska = "greska"
            return greska
        if danUNedeljiInt == PONEDELJAK:
            danUNedelji = "pon"
        elif danUNedeljiInt == UTORAK:
            danUNedelji = "uto"
        elif danUNedeljiInt == SREDA:
            danUNedelji = "sre"
        elif danUNedeljiInt == CETVRTAK:
            danUNedelji = "cet"
        elif danUNedeljiInt == PETAK:
            danUNedelji = "pet"
        elif danUNedeljiInt == SUBOTA:
            danUNedelji = "sub"
        elif danUNedeljiInt == NEDELJA:
            danUNedelji = "ned"

        return danUNedelji

    def vezani_let(self, nazivLeta):
        dostupniLetovi = []
        odrediste = ""
        ukupnoVremeDolaska = 0

        letRedovi = datoteka.procitaj_datoteku("letovi.txt")
        for let in letRedovi:
            letRed = let.split("|")
            if letRed[0] == nazivLeta:
                odrediste = letRed[2]
                vremeDolaska = letRed[4].split(":")
                satDolaska = int(vremeDolaska[0])
                minutDolaska = int(vremeDolaska[1])
                ukupnoVremeDolaska = satDolaska * 60 + minutDolaska

        for let in letRedovi:
            letRed = let.split("|")
            dolaziste = letRed[1]
            vremePolaska = letRed[3].split(":")
            satPolaska = int(vremePolaska[0])
            minutPolaska = int(vremePolaska[1])
            razlika = ukupnoVremeDolaska - (satPolaska * 60 + minutPolaska)
            if (odrediste == dolaziste) and (razlika < 60):
                dostupniLetovi.append(let)
        return dostupniLetovi

    def prtraga_karata_po_nazivu_leta(self, nazivLeta):

        pronadjeneKarte = []

        karteRedovi = datoteka.procitaj_datoteku("karte.txt")
        for karta in karteRedovi:
            kartaRed = karta.split("|")
            if nazivLeta == kartaRed[0]:
                pronadjeneKarte.append(karta)

        return pronadjeneKarte