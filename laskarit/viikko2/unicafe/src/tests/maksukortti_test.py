import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertNotEqual(str(self.maksukortti), "Kortilla on rahaa 100.00 euroa")
    
    def test_lataaminen_toimii(self):
        kortti = Maksukortti(0)
        kortti.lataa_rahaa(1200)
        self.assertEqual(str(kortti), "Kortilla on rahaa 12.00 euroa")
    
    def test_saldo_vahenee_jos_tarpeeksi(self):
        kortti = Maksukortti(1000)
        totuusarvo = kortti.ota_rahaa(100)
        self.assertEqual(str(kortti), "Kortilla on rahaa 9.00 euroa")
        self.assertEqual(totuusarvo, True)
    
    def test_saldo_ei_vahene_jossei_riittavasti(self):
        kortti = Maksukortti(100)
        kortti.ota_rahaa(1000)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(kortti.ota_rahaa(1000), False)