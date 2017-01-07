import unittest
from korisnik import *


class TestKorisnik(unittest.TestCase):
    def setUp(self):
        self.korisnikServis = KorisnikServis()

    def test_login_radi(self):
        rezultat = self.korisnikServis.login("misa", "ds")
        assert rezultat == True

    def test_login_ne_radi(self):
        rezultat = self.korisnikServis.login("misa", "neka_lozinka")
        assert rezultat == False

    def test_vraca_korektnu_ulogu(self):
        uloga = self.korisnikServis.vratiUlogu("misa")
        assert uloga == "menadzer"

    def test_vraca_none_za_nepostojeceg_korisnika(self):
        uloga = self.korisnikServis.vratiUlogu("jackie")
        assert uloga is None
