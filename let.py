import datoteka
import datetime


class Let:
    def __init__(self, nazivLeta, polaziste, odrediste, vremePolaska, vremeDolaska, prevoznik, dan, brojSedista, cena):
        self.nazivLeta = nazivLeta
        self.polaziste = polaziste
        self.odrediste = odrediste
        self.vremePolaska = vremePolaska
        self.vremeDolaska = vremeDolaska
        self.prevoznik = prevoznik
        self.dan = dan
        self.brojSedista = brojSedista
        self.cena = cena

    def print_let(self):
        print(
            self.nazivLeta + "|" + self.polaziste + "|" + self.odrediste + "|" + self.vremePolaska + "|"
            + self.vremeDolaska + "|" + self.prevoznik + "|" + self.dan + "|" + self.brojSedista + "|" + self.cena)

    def vrati_naziv_leta(self):
        return self.nazivLeta

    def vrati_polaziste(self):
        return self.polaziste

    def vrati_odrediste(self):
        return self.odrediste

    def vrati_vreme_polaska(self):
        return self.vremePolaska

    def vrati_vreme_dolaska(self):
        return self.vremeDolaska

    def vrati_prevoznika(self):
        return self.prevoznik

    def vrati_dan(self):
        return self.dan

    def vrati_broj_sedista(self):
        return self.brojSedista

    def vrati_cenu(self):
        return self.cena


class LetServis:
    listaLetova = []
    OPCIJA_PRETRAGE_POLAZISTE = "polaziste"
    OPCIJA_PRETRAGE_ODREDISTE = "odrediste"
    OPCIJA_PRETRAGE_VREME_POLETANJA = "vreme poletanja"
    OPCIJA_PRETRAGE_VREME_SLETANJA = "vreme sletanja"
    OPCIJA_PRETRAGE_PREVOZNIKU = "prevoznik"

    def inicijalizuj_letove(self):
        letoviRedovi = datoteka.procitaj_datoteku("letovi.txt")
        for letRed in letoviRedovi:
            let = letRed.split("|")
            procitaniLet = Let(let[0], let[1], let[2], let[3], let[4], let[5], let[6], let[7], let[8])
            self.listaLetova.append(procitaniLet)
        return self.listaLetova

    def pretraga_leta(self, unesenaOpcija, opcijaPretrage):
        pronadjeniLetovi = []

        if opcijaPretrage == LetServis.OPCIJA_PRETRAGE_POLAZISTE:
            for let in self.listaLetova:
                if unesenaOpcija == let.vrati_polaziste():
                    pronadjeniLetovi.append(let)
        elif opcijaPretrage == LetServis.OPCIJA_PRETRAGE_ODREDISTE:
            for let in self.listaLetova:
                if unesenaOpcija == let.vrati_odrediste():
                    pronadjeniLetovi.append(let)
        elif opcijaPretrage == LetServis.OPCIJA_PRETRAGE_VREME_POLETANJA:
            for let in self.listaLetova:
                if unesenaOpcija == let.vrati_vreme_polaska():
                    pronadjeniLetovi.append(let)
        elif opcijaPretrage == LetServis.OPCIJA_PRETRAGE_VREME_SLETANJA:
            for let in self.listaLetova:
                if unesenaOpcija == let.vrati_vreme_dolaska():
                    pronadjeniLetovi.append(let)
        elif opcijaPretrage == LetServis.OPCIJA_PRETRAGE_PREVOZNIKU:
            for let in self.listaLetova:
                if unesenaOpcija == let.vrati_prevoznika():
                    pronadjeniLetovi.append(let)

        return pronadjeniLetovi

    def pretraga_leta_po_datumu_polaska(self, datumPolaska):
        pronadjeniLetovi = []
        danUNedelji = self.dan_u_nedelji(datumPolaska)

        for let in self.listaLetova:
            daniLeta = str(let.vrati_dan()).split(",")
            for dan in daniLeta:
                if dan == danUNedelji:
                    pronadjeniLetovi.append(let)
        return pronadjeniLetovi

    def pretraga_leta_po_datumu_dolaska(self, datumDolaska):
        pronadjeniLetovi = []
        danUNedelji = self.dan_u_nedelji(datumDolaska)
        jucerasnjiDanUNedelji = ""
        if danUNedelji == "pon":
            jucerasnjiDanUNedelji = "ned"
        elif danUNedelji == "uto":
            jucerasnjiDanUNedelji = "pon"
        elif danUNedelji == "sre":
            jucerasnjiDanUNedelji = "uto"
        elif danUNedelji == "cet":
            jucerasnjiDanUNedelji = "sre"
        elif danUNedelji == "pet":
            jucerasnjiDanUNedelji = "cet"
        elif danUNedelji == "sub":
            jucerasnjiDanUNedelji = "pet"
        elif danUNedelji == "ned":
            jucerasnjiDanUNedelji = "sub"

        for let in self.listaLetova:
            daniLeta = str(let.vrati_dan()).split(",")
            vremePolaskaLista = let.vrati_vreme_polaska().split(":")
            satPolaska = int(vremePolaskaLista[0])
            vremeDolaskaLista = let.vrati_vreme_dolaska().split(":")
            satDolaska = int(vremeDolaskaLista[0])
            for dan in daniLeta:
                if (dan == jucerasnjiDanUNedelji) and (satPolaska > satDolaska):
                    pronadjeniLetovi.append(let)
            for dan in daniLeta:
                if (dan == danUNedelji) and (satDolaska >= satPolaska) and (satDolaska < 24):
                    pronadjeniLetovi.append(let)
        return pronadjeniLetovi

    def prikazi_slobodna_sedista(self, nazivLeta, datumPolaska, kartaServis):

        abc = [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]
        brojRedova = 0
        brojKolona = 0
        zauzetaMesta = kartaServis.zauzeta_sedista(nazivLeta, datumPolaska)
        for let in self.listaLetova:
            if let.vrati_naziv_leta() == nazivLeta:
                kolRed = let.vrati_broj_sedista().split("/")
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

    def cena_karte(self, nazivLeta):
        cena = ""
        for let in self.listaLetova:
            if let.vrati_naziv_leta() == nazivLeta:
                cena = let.vrati_cenu()
        return cena

    def vezani_let(self, nazivLeta):
        dostupniLetovi = []
        odrediste = ""
        ukupnoVremeDolaska = 0

        for let in self.listaLetova:
            if let.vrati_naziv_leta() == nazivLeta:
                odrediste = let.vrati_odrediste()
                vremeDolaska = let.vrati_vreme_dolaska().split(":")
                satDolaska = int(vremeDolaska[0])
                minutDolaska = int(vremeDolaska[1])
                ukupnoVremeDolaska = satDolaska * 60 + minutDolaska

        for let in self.listaLetova:
            polaziste = let.vrati_polaziste()
            vremePolaska = let.vrati_vreme_polaska().split(":")
            satPolaska = int(vremePolaska[0])
            minutPolaska = int(vremePolaska[1])
            razlika = (satPolaska * 60 + minutPolaska) - ukupnoVremeDolaska
            if (odrediste == polaziste) and (razlika < 60):
                dostupniLetovi.append(let)
        return dostupniLetovi

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
        try:
            datumLetaLista = datumLeta.split("/")
            godina = int(datumLetaLista[0])
            mesec = int(datumLetaLista[1])
            dan = int(datumLetaLista[2])
            danUNedeljiInt = datetime.date(godina, mesec, dan).weekday()
        except IndexError:
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

    def nepostojeci_naziv_leta(self, nazivLeta):
        greska = True
        for let in self.listaLetova:
            if nazivLeta == let.vrati_naziv_leta():
                greska = False

        return greska
