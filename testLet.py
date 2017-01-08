import unittest
from let import *


class TestLet(unittest.TestCase):
    def setUp(self):
        self.letServis = LetServis()

    def test_pretraga_po_polazistu_radi(self):
        pronadjeniLetovi = self.letServis.pretragaLeta("KZN", LetServis.OPCIJA_PRETRAGE_POLAZISTE)
        assert len(pronadjeniLetovi) == 28

        pronadjeniLetovi2 = self.letServis.pretragaLeta("NE_POSTOJI", LetServis.OPCIJA_PRETRAGE_POLAZISTE)
        assert len(pronadjeniLetovi2) == 0

    def test_pretraga_po_odredistu_radi(self):
        pronadjeniLetovi = self.letServis.pretragaLeta("LED", LetServis.OPCIJA_PRETRAGE_ODREDISTE)
        assert len(pronadjeniLetovi) == 184

        pronadjeniLetovi2 = self.letServis.pretragaLeta("NE_POSTOJI", LetServis.OPCIJA_PRETRAGE_ODREDISTE)
        assert len(pronadjeniLetovi2) == 0

    def test_pretraga_po_vremenu_poletanja_radi(self):
        pronadjeniLetovi = self.letServis.pretragaLeta("13:30", LetServis.OPCIJA_PRETRAGE_VREME_POLETANJA)
        assert len(pronadjeniLetovi) == 667

        pronadjeniLetovi2 = self.letServis.pretragaLeta("NE_POSTOJI", LetServis.OPCIJA_PRETRAGE_VREME_POLETANJA)
        assert len(pronadjeniLetovi2) == 0

    def test_pretraga_po_vremenu_sletanja_radi(self):
        pronadjeniLetovi = self.letServis.pretragaLeta("13:30", LetServis.OPCIJA_PRETRAGE_VREME_SLETANJA)
        assert len(pronadjeniLetovi) == 655

        pronadjeniLetovi2 = self.letServis.pretragaLeta("NE_POSTOJI", LetServis.OPCIJA_PRETRAGE_VREME_SLETANJA)
        assert len(pronadjeniLetovi2) == 0

    def test_pretraga_po_prevozniku_radi(self):
        pronadjeniLetovi = self.letServis.pretragaLeta("Aero Flight", LetServis.OPCIJA_PRETRAGE_PREVOZNIKU)
        assert len(pronadjeniLetovi) == 34

        pronadjeniLetovi2 = self.letServis.pretragaLeta("NE_POSTOJI", LetServis.OPCIJA_PRETRAGE_PREVOZNIKU)
        assert len(pronadjeniLetovi2) == 0
