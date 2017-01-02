# korisnicko ime, lozinka, prezime, uloga(prodavac, menadzer)

class Korisnik:
    # vraca samo ulogu korisnika
    def info(self, indexKorisnika):
        korisnici = open("korisnici", "r")
        kor = korisnici.readlines()
        osobe = (kor[indexKorisnika])
        korisnikInfo = osobe.split("|")
        korUloga = korisnikInfo[3]
        return korUloga

    # ispisuje podatke o ulogovanom korisniku
    def informacije(self, indexKorisnika):
        korisnici = open("korisnici", "r")
        kor = korisnici.readlines()
        osobe = (kor[indexKorisnika])
        korisnikInfo = osobe.split("|")
        korisnickoIme = korisnikInfo[0]
        ime = korisnikInfo[1]
        prezime = korisnikInfo[2]
        uloga = korisnikInfo[3]

        print("Korisnicko ime: ", korisnickoIme)
        print("Ime:", ime)
        print("Prezime:", prezime)
        print("Uloga:", uloga)


class Avion:
    def __init__(self, naziv, brojRed, brojSed):
        self.naziv = naziv
        self.brojRed = brojRed
        self.brojSed = brojSed

    def mesta(self):
        brojMesta = self.brojRed * self.brojSed
        return brojMesta
