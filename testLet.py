import unittest
from let import *


class TestLet(unittest.TestCase):
    def setUp(self):
        self.letServis = LetServis()

    def test_pretraga_po_odredistu_radi(self):
        pronadjeniLetovi = self.letServis.pretragaLeta("KZN", LetServis.OPCIJA_PRETRAGE_POLAZISTE)
        assert len(pronadjeniLetovi) == 28

        pronadjeniLetovi2 = self.letServis.pretragaLeta("NE_POSTOJI", LetServis.OPCIJA_PRETRAGE_POLAZISTE)
        assert len(pronadjeniLetovi2) == 0