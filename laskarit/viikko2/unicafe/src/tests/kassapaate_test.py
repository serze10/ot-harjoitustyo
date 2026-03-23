import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_alussa_raha_ja_lounaat_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        # euroina-metodi palauttaa oikean luvun (alkusaldo 1000 euroa)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_kateisosto_edullinen_riittava(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(vaihtoraha, 500 - 240)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000 + 2.40, places=2)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_maukas_riittava(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 500 - 400)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000 + 4.00, places=2)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_ei_riittava(self):
        alku = self.kassapaate.kassassa_rahaa_euroina()
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), alku)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_maukas_ei_riittava(self):
        alku = self.kassapaate.kassassa_rahaa_euroina()
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), alku)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_edullinen_riittava(self):
        result = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertTrue(result)
        self.assertEqual(self.kortti.saldo, 1000 - 240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        # kortilla ostettaessa kassan rahamaara ei muutu
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_korttiosto_maukas_riittava(self):
        result = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertTrue(result)
        self.assertEqual(self.kortti.saldo, 1000 - 400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_korttiosto_ei_riittava(self):
        huono_kortti = Maksukortti(100)
        result = self.kassapaate.syo_maukkaasti_kortilla(huono_kortti)
        self.assertFalse(result)
        self.assertEqual(huono_kortti.saldo, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_korttiosto_edullinen_ei_riittava(self):
        huono_kortti = Maksukortti(100)
        result = self.kassapaate.syo_edullisesti_kortilla(huono_kortti)
        self.assertFalse(result)
        self.assertEqual(huono_kortti.saldo, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_lataa_rahaa_kortille_kasvattaa_saldoa_ja_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 2500)
        self.assertEqual(self.kortti.saldo, 1000 + 2500)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000 + 25.0, places=2)

    def test_lataa_negatiivinen_ei_muuta(self):
        alku_kortin_saldo = self.kortti.saldo
        alku_kassa = self.kassapaate.kassassa_rahaa_euroina()
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kortti.saldo, alku_kortin_saldo)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), alku_kassa)


if __name__ == '__main__':
    unittest.main()
