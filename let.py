import datoteka


class LetServis:

    OPCIJA_PRETRAGE_POLAZISTE = "polaziste"
    OPCIJA_PRETRAGE_ODREDISTE = "odrediste"
    OPCIJA_PRETRAGE_VREME_POLETANJA = "vreme poletanja"
    OPCIJA_PRETRAGE_VREME_SLETANJA = "vreme sletanja"
    OPCIJA_PRETRAGE_PREVOZNIKU = "prevoznik"

    def pretraga_leta(self, input, opcijaPretrage):
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
            if input == letRed[indexPolja]:
                pronadjeniLetovi.append(letRed)

        return pronadjeniLetovi
