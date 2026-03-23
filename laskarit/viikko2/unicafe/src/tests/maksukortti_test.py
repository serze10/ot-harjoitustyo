import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(2500)
        self.assertEqual(self.maksukortti.saldo, 3500)

    def test_ota_rahaa_vahentaa_saldoa_jos_riittavasti(self):
        result = self.maksukortti.ota_rahaa(500)
        self.assertTrue(result)
        self.assertEqual(self.maksukortti.saldo, 500)

    def test_ota_rahaa_ei_muuta_saldoa_jos_ei_riittavasti(self):
        result = self.maksukortti.ota_rahaa(2000)
        self.assertFalse(result)
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_ota_rahaa_palauttaa_true_ja_false(self):
        self.assertTrue(self.maksukortti.ota_rahaa(1000))
        self.assertFalse(self.maksukortti.ota_rahaa(1))
