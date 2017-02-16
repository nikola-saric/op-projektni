import datoteka


class KorisnikServis:
    # funkcija vraca True ako su kredencijali tacni, False ako nisu
    def login(self, korisnickoImeInput, lozinkaInput):
        korisniciRedovi = datoteka.procitaj_datoteku("korisnici.txt")
        korisnickaImena = []

        for i in range(len(korisniciRedovi)):
            korisnikRed = (korisniciRedovi[i])
            osobelista = korisnikRed.split("|")
            korisnickaImena.append(osobelista[0])

        pronadjenoKorisnickoIme = ""
        for korImeFajl in korisnickaImena:
            if korImeFajl == korisnickoImeInput:
                pronadjenoKorisnickoIme = korisnickoImeInput

        if pronadjenoKorisnickoIme == "":
            return False

        lozinke = datoteka.procitaj_datoteku("lozinke.txt")
        for lozinkaRed in lozinke:
            red = lozinkaRed.split("|")
            korisnickoIme = red[0]
            lozinka = red[1]
            if (korisnickoIme == pronadjenoKorisnickoIme) and (lozinkaInput == lozinka):
                return True

        return False

    def vrati_ulogu(self, korisnickoIme):
        korisniciRedovi = datoteka.procitaj_datoteku("korisnici.txt")
        for korisnik in korisniciRedovi:
            korisnikPodaci = korisnik.split("|")
            if korisnikPodaci[0] == korisnickoIme:
                return korisnikPodaci[3]

    def vrati_ime(self, korisnickoIme):
        korisniciRedovi = datoteka.procitaj_datoteku("korisnici.txt")
        for korisnik in korisniciRedovi:
            korisnikPodaci = korisnik.split("|")
            if korisnikPodaci[0] == korisnickoIme:
                return korisnikPodaci[1]

        return None
