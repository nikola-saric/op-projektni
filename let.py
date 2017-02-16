import datoteka


class LetServis:
    OPCIJA_PRETRAGE_POLAZISTE = "polaziste"
    OPCIJA_PRETRAGE_ODREDISTE = "odrediste"
    OPCIJA_PRETRAGE_VREME_POLETANJA = "vreme poletanja"
    OPCIJA_PRETRAGE_VREME_SLETANJA = "vreme sletanja"
    OPCIJA_PRETRAGE_PREVOZNIKU = "prevoznik"

    def pretraga_leta(self, unesenaOpcija, opcijaPretrage):
        indexPolja = -1

        if opcijaPretrage == LetServis.OPCIJA_PRETRAGE_POLAZISTE:
            indexPolja = 1
        elif opcijaPretrage == LetServis.OPCIJA_PRETRAGE_ODREDISTE:
            indexPolja = 2
        elif opcijaPretrage == LetServis.OPCIJA_PRETRAGE_VREME_POLETANJA:
            indexPolja = 3
        elif opcijaPretrage == LetServis.OPCIJA_PRETRAGE_VREME_SLETANJA:
            indexPolja = 4
        elif opcijaPretrage == LetServis.OPCIJA_PRETRAGE_PREVOZNIKU:
            indexPolja = 5

        pronadjeniLetovi = []

        letRedovi = datoteka.procitaj_datoteku("letovi.txt")
        for let in letRedovi:
            letRed = let.split("|")
            if unesenaOpcija == letRed[indexPolja]:
                pronadjeniLetovi.append(letRed)

        return pronadjeniLetovi

    def pretraga_leta_po_datumu_polaska(self, datumPolaska, kartaServis):
        pronadjeniLetovi = []
        danUNedelji = kartaServis.dan_u_nedelji(datumPolaska)

        letRedovi = datoteka.procitaj_datoteku("letovi.txt")
        for let in letRedovi:
            letRed = let.split("|")
            daniLeta = letRed[6].split(",")
            for dan in daniLeta:
                if dan == danUNedelji:
                    pronadjeniLetovi.append(letRed)
        return pronadjeniLetovi

    def pretraga_leta_po_datumu_dolaska(self, datumDolaska, kartaServis):
        pronadjeniLetovi = []
        danUNedelji = kartaServis.dan_u_nedelji(datumDolaska)
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

        letRedovi = datoteka.procitaj_datoteku("letovi.txt")
        for let in letRedovi:
            letRed = let.split("|")
            daniLeta = letRed[6].split(",")
            vremePolaskaLista = letRed[3].split(":")
            satPolaska = int(vremePolaskaLista[0])
            vremeDolaskaLista = letRed[4].split(":")
            satDolaska = int(vremeDolaskaLista[0])
            for dan in daniLeta:
                if (dan == jucerasnjiDanUNedelji) and (satPolaska > satDolaska):
                    pronadjeniLetovi.append(letRed)
            for dan in daniLeta:
                if (dan == danUNedelji) and (satDolaska >= satPolaska) and (satDolaska < 24):
                    pronadjeniLetovi.append(letRed)
        return pronadjeniLetovi
