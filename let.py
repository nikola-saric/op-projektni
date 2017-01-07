import filecitac
class LetServis:

    OPCIJA_PRETRAGE_POLAZISTE = "polaziste"
    OPCIJA_PRETRAGE_ODREDISTE = "odrediste"

    def pretragaLeta(self, input, opcijaPretrage):
        indexPolja = -1

        if opcijaPretrage == LetServis.OPCIJA_PRETRAGE_POLAZISTE:
            indexPolja = 1
        elif opcijaPretrage == LetServis.OPCIJA_PRETRAGE_ODREDISTE:
            indexPolja = 2

        pronadjeniLetovi = []

        letRedovi = filecitac.procitajDatoteku("letovi.txt")
        for let in letRedovi:
            letRed = let.split("|")
            if input == letRed[indexPolja]:
                pronadjeniLetovi.append(letRed)

        return pronadjeniLetovi
