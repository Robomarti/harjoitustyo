import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
    
    def test_kassa_luotu(self):
        self.assertNotEqual(self.kassa, None)
    
    def test_kassa_luotu_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_edullinen_kateisosto_toimii_kun_maksu_riittaa(self):
        kassa = Kassapaate()
        vaihtoraha = kassa.syo_edullisesti_kateisella(400)
        self.assertEqual(vaihtoraha, 160)
        self.assertEqual(kassa.kassassa_rahaa, 100240)
        self.assertEqual(kassa.edulliset, 1)
    
    def test_edullinen_kateisosto_toimii_kun_maksu_ei_riita(self):
        kassa = Kassapaate()
        vaihtoraha = kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(kassa.kassassa_rahaa, 100000)
        self.assertEqual(kassa.edulliset, 0)

    def test_maukas_kateisosto_toimii_kun_maksu_riittaa(self):
        kassa = Kassapaate()
        vaihtoraha = kassa.syo_maukkaasti_kateisella(600)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(kassa.kassassa_rahaa, 100400)
        self.assertEqual(kassa.maukkaat, 1)
    
    def test_maukas_kateisosto_toimii_kun_maksu_ei_riita(self):
        kassa = Kassapaate()
        vaihtoraha = kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(kassa.kassassa_rahaa, 100000)
        self.assertEqual(kassa.maukkaat, 0)
    
    def test_edullinen_korttiosto_toimii_kun_maksu_riittaa(self):
        kassa = Kassapaate()
        kortti = Maksukortti(400)
        onnistuiko = kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(onnistuiko, True)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.60 euroa")
        self.assertEqual(kassa.kassassa_rahaa, 100000)
        self.assertEqual(kassa.edulliset, 1)
    
    def test_edullinen_korttiosto_toimii_kun_maksu_ei_riita(self):
        kassa = Kassapaate()
        kortti = Maksukortti(100)
        onnistuiko = kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(onnistuiko, False)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(kassa.kassassa_rahaa, 100000)
        self.assertEqual(kassa.edulliset, 0)

    def test_maukas_korttisosto_toimii_kun_maksu_riittaa(self):
        kassa = Kassapaate()
        kortti = Maksukortti(450)
        onnistuiko = kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(onnistuiko, True)
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.50 euroa")
        self.assertEqual(kassa.kassassa_rahaa, 100000)
        self.assertEqual(kassa.maukkaat, 1)
    
    def test_maukas_korttiosto_toimii_kun_maksu_ei_riita(self):
        kassa = Kassapaate()
        kortti = Maksukortti(100)
        onnistuiko = kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(onnistuiko, False)
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(kassa.kassassa_rahaa, 100000)
        self.assertEqual(kassa.maukkaat, 0)
    
    def test_lataa_rahaa_kortille_onnistuneesti(self):
        kassa = Kassapaate()
        kortti = Maksukortti(400)
        kassa.lataa_rahaa_kortille(kortti, 400)
        self.assertEqual(str(kortti), "Kortilla on rahaa 8.00 euroa")
        self.assertEqual(kassa.kassassa_rahaa, 100400)

    def test_lataa_rahaa_kortille_epaonnistuneesti(self):
        kassa = Kassapaate()
        kortti = Maksukortti(400)
        kassa.lataa_rahaa_kortille(kortti, -400)
        self.assertEqual(str(kortti), "Kortilla on rahaa 4.00 euroa")
        self.assertEqual(kassa.kassassa_rahaa, 100000)