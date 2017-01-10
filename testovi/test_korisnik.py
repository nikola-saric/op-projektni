import unittest
from korisnik import *

class TestKorisnik(unittest.TestCase):
    def setUp(self):
        datoteka.test_mode = True
        self.korisnikServis = KorisnikServis()

    def tearDown(self):
        datoteka.test_mode = False

    def test_login_radi(self):
        rezultat = self.korisnikServis.login("misa", "misa_sifra")
        assert rezultat == True

    def test_login_ne_radi(self):
        rezultat = self.korisnikServis.login("misa", "neka_lozinka")
        assert rezultat == False

    def test_vraca_korektnu_ulogu(self):
        uloga = self.korisnikServis.vrati_ulogu("misa")
        assert uloga == "menadzer"

    def test_vraca_none_za_nepostojeceg_korisnika(self):
        uloga = self.korisnikServis.vrati_ulogu("jackie")
        assert uloga is None
