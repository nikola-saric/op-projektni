import datoteka
import datetime


class Karta:
    def __init__(self, nazivLeta, imePutnika, prezimePutnika, drzavPutnika, brojPasosaPutnika, datumPolaskaLeta,
                 sediste,
                 imeProdavca, datumIzdavanja, cena):
        self.nazivLeta = nazivLeta
        self.imePutnika = imePutnika
        self.prezimePutnika = prezimePutnika
        self.drzavPutnika = drzavPutnika
        self.brojPasosaPutnika = brojPasosaPutnika
        self.datumPolaskaLeta = datumPolaskaLeta
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
        print("Datum leta: ", self.datumPolaskaLeta)
        print("Vase sediste je: ", self.sediste)
        print("Ime prodavca: ", self.imeProdavca)
        print("Datum izdavanja: ", self.datumIzdavanja)
        print("Cena karte: ", self.cena)
        print("============\n")

    def upisi_kartu(self):
        kartaStr = self.nazivLeta + "|" + self.imePutnika + "|" + self.prezimePutnika + "|" + self.drzavPutnika + "|" + \
                   self.brojPasosaPutnika + "|" + self.datumPolaskaLeta + "|" + self.sediste + "|" + self.imeProdavca + "|" + \
                   self.datumIzdavanja + "|" + self.cena + "\n"

        datoteka.upisi_u_datoteku("karte.txt", kartaStr)

    def vrati_naziv_leta(self):
        return self.nazivLeta

    def vrati_ime_putnika(self):
        return self.imePutnika

    def vrati_prezime_putnika(self):
        return self.prezimePutnika

    def vrati_drzavljanstvo_putnika(self):
        return self.drzavPutnika

    def vrati_broj_pasosa_putnika(self):
        return self.brojPasosaPutnika

    def vrati_datum_polaska_leta(self):
        return self.datumPolaskaLeta

    def vrati_sediste(self):
        return self.sediste

    def vrati_ime_prodavca(self):
        return self.imeProdavca

    def vrati_datum_izdavanja(self):
        return self.datumIzdavanja

    def vrati_cenu(self):
        return self.cena


class KartaServis:
    listaRezervisanihKarata = []

    # ucitava sve karte iz karte.txt.

    def inicijalizuj_karte(self):
        karteRedovi = datoteka.procitaj_datoteku("karte.txt")
        for kartaRed in karteRedovi:
            karta = kartaRed.split("|")
            procitanaKarta = Karta(karta[0], karta[1], karta[2], karta[3], karta[4], karta[5], karta[6], karta[7],
                                   karta[8], karta[9])
            self.listaRezervisanihKarata.append(procitanaKarta)
        return self.listaRezervisanihKarata

    def obrisi_kartu(self, nazivLetaKarta, brojPasosaKarta, datumPolaska):
        nepostojecaKarta = True
        for karta in self.listaRezervisanihKarata:
            if (nazivLetaKarta == karta.vrati_naziv_leta()) and (
                        brojPasosaKarta == karta.vrati_broj_pasosa_putnika()) and (
                        datumPolaska == karta.vrati_datum_polaska_leta()):
                self.listaRezervisanihKarata.remove(karta)
                nepostojecaKarta = False

        return nepostojecaKarta

    def izmeni_kartu(self, nazivLetaKarta, brojPasosaKarta, datumPolaska, noviNazivLeta, noviDatumLeta, novoSediste):
        nepostojecaKarta = True

        for karta in self.listaRezervisanihKarata:
            if (nazivLetaKarta == karta.vrati_naziv_leta()) and (
                        brojPasosaKarta == karta.vrati_broj_pasosa_putnika()) and (
                        datumPolaska == karta.vrati_datum_polaska_leta()):
                staroIme = karta.vrati_ime_putnika()
                staroPrezime = karta.vrati_prezime_putnika()
                staroDrzavljanstvo = karta.vrati_drzavljanstvo_putnika()
                staroImeProdavca = karta.vrati_ime_prodavca()
                stariDatumIzdavanja = karta.vrati_datum_izdavanja()
                staraCena = karta.vrati_cenu()
                novaKarta = Karta(noviNazivLeta, staroIme, staroPrezime, staroDrzavljanstvo, brojPasosaKarta,
                                  noviDatumLeta, novoSediste, staroImeProdavca, stariDatumIzdavanja, staraCena)
                self.listaRezervisanihKarata.append(novaKarta)
                self.listaRezervisanihKarata.remove(karta)
                nepostojecaKarta = False

                return nepostojecaKarta

        return nepostojecaKarta

    def prodate_karte_za_izabrani_dan_prodaje_ili_polaska(self, izabraniDan, izabranaOpcija):
        DAN_PRODAJE = 1
        DAN_POLASKA = 2
        pronadjeneKarte = []

        if izabranaOpcija == DAN_PRODAJE:
            for karta in self.listaRezervisanihKarata:

                if izabraniDan == karta.vrati_datum_izdavanja():
                    pronadjeneKarte.append(karta)

        elif izabranaOpcija == DAN_POLASKA:
            for karta in self.listaRezervisanihKarata:

                if izabraniDan == karta.vrati_datum_polaska_leta():
                    pronadjeneKarte.append(karta)

        return pronadjeneKarte

    def prodate_karte_za_izabrani_dan_prodaje_i_izabranog_prodavca(self, izabraniDan, izabraniProdavac):

        pronadjeneKarte = []
        for karta in self.listaRezervisanihKarata:
            if (izabraniDan == karta.vrati_datum_izdavanja()) and (izabraniProdavac == karta.vrati_ime_prodavca()):
                pronadjeneKarte.append(karta)
        return pronadjeneKarte

    def ukupan_broj_prodatih_karata_i_cena_za_izabrani_dan_prodaje_i_polaska(self, izabraniDan, izabranaOpcija):
        DAN_PRODAJE = 4
        DAN_POLASKA = 5
        ukupnaCena = 0
        brojKarata = 0
        if izabranaOpcija == DAN_PRODAJE:
            for karta in self.listaRezervisanihKarata:
                if izabraniDan == karta.vrati_datum_izdavanja():
                    brojKarata += 1
                    cenaKarte = int(karta.vrati_cenu())
                    ukupnaCena += cenaKarte

        elif izabranaOpcija == DAN_POLASKA:
            for karta in self.listaRezervisanihKarata:
                if izabraniDan == karta.vrati_datum_polaska_leta():
                    brojKarata += 1
                    cenaKarte = int(karta.vrati_cenu())
                    ukupnaCena += cenaKarte

        return brojKarata, ukupnaCena

    def ukupan_broj_prodatih_karata_i_cena_za_izabrani_dan_prodaje_i_prodavca(self, izabraniDan, izabraniProdavac):
        ukupnaCena = 0
        brojKarata = 0

        for karta in self.listaRezervisanihKarata:
            if (izabraniProdavac == karta.vrati_ime_prodavca()) and (izabraniDan == karta.vrati_datum_izdavanja()):
                brojKarata += 1
                cenaKarte = int(karta.vrati_cenu())
                ukupnaCena += cenaKarte

        return brojKarata, ukupnaCena

    def ukupan_broj_prodatih_karat_i_cena_po_prodavcu_poslednjih_30_dana(self, izabraniProdavac):
        ukupnaCena = 0
        brojKarata = 0
        danasnjiDatum = datetime.date.today()

        for karta in self.listaRezervisanihKarata:
            datumProdaje = karta.vrati_datum_izdavanja()
            intDatumProdajeLista = datumProdaje.split("-")
            godina = int(intDatumProdajeLista[0])
            mesec = int(intDatumProdajeLista[1])
            dan = int(intDatumProdajeLista[2])
            intDatumProdaje = datetime.date(godina, mesec, dan)
            datum = danasnjiDatum - intDatumProdaje
            datumDays = datum.days
            if (izabraniProdavac == karta.vrati_ime_prodavca()) and (datumDays <= 30):
                brojKarata += 1
                cenaKarte = int(karta.vrati_cenu())
                ukupnaCena += cenaKarte

        return brojKarata, ukupnaCena

    def zauzeta_sedista(self, nazivLeta, datumPolaska):
        zauzetaMesta = []
        for karta in self.listaRezervisanihKarata:
            if (nazivLeta == karta.vrati_naziv_leta()) and (datumPolaska == karta.vrati_datum_polaska_leta()):
                zauzetaMesta.append(karta.vrati_sediste())

        return zauzetaMesta

    def pretraga_karata_po_nazivu_leta(self, nazivLeta):

        pronadjeneKarte = []

        for karta in self.listaRezervisanihKarata:
            if nazivLeta == karta.vrati_naziv_leta():
                pronadjeneKarte.append(karta)

        return pronadjeneKarte

    def snimi_karte_u_fajl(self):
        karteFile = open("karte.txt", "w")
        for karta in self.listaRezervisanihKarata:
            karta.upisi_kartu()
        karteFile.close()
