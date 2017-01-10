import unittest
from let import *

class TestLet(unittest.TestCase):

    def setUp(self):
        datoteka.test_mode = True
        self.letServis = LetServis()

    def tearDown(self):
        datoteka.test_mode = False

    def test_pretraga_po_polazistu_radi(self):
        pronadjeniLetovi = self.letServis.pretraga_leta("KZN", LetServis.OPCIJA_PRETRAGE_POLAZISTE)
        assert len(pronadjeniLetovi) == 28

        pronadjeniLetovi2 = self.letServis.pretraga_leta("NE_POSTOJI", LetServis.OPCIJA_PRETRAGE_POLAZISTE)
        assert len(pronadjeniLetovi2) == 0

    def test_pretraga_po_odredistu_radi(self):
        pronadjeniLetovi = self.letServis.pretraga_leta("LED", LetServis.OPCIJA_PRETRAGE_ODREDISTE)
        assert len(pronadjeniLetovi) == 184

        pronadjeniLetovi2 = self.letServis.pretraga_leta("Abrakadabra", LetServis.OPCIJA_PRETRAGE_ODREDISTE)
        assert len(pronadjeniLetovi2) == 0

    def test_pretraga_po_vremenu_poletanja_radi(self):
        pronadjeniLetovi = self.letServis.pretraga_leta("13:30", LetServis.OPCIJA_PRETRAGE_VREME_POLETANJA)
        assert len(pronadjeniLetovi) == 667

        pronadjeniLetovi2 = self.letServis.pretraga_leta("NE_POSTOJI", LetServis.OPCIJA_PRETRAGE_VREME_POLETANJA)
        assert len(pronadjeniLetovi2) == 0

    def test_pretraga_po_vremenu_sletanja_radi(self):
        pronadjeniLetovi = self.letServis.pretraga_leta("13:30", LetServis.OPCIJA_PRETRAGE_VREME_SLETANJA)
        assert len(pronadjeniLetovi) == 655

        pronadjeniLetovi2 = self.letServis.pretraga_leta("NE_POSTOJI", LetServis.OPCIJA_PRETRAGE_VREME_SLETANJA)
        assert len(pronadjeniLetovi2) == 0

    def test_pretraga_po_prevozniku_radi(self):
        pronadjeniLetovi = self.letServis.pretraga_leta("Aero Flight", LetServis.OPCIJA_PRETRAGE_PREVOZNIKU)
        assert len(pronadjeniLetovi) == 34

        pronadjeniLetovi2 = self.letServis.pretraga_leta("Macak u cizmama", LetServis.OPCIJA_PRETRAGE_PREVOZNIKU)
        assert len(pronadjeniLetovi2) == 0

