import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote
from ostoskori import Ostoskori

class TestKauppa(unittest.TestCase):
    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan_oikein(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5) 
    
    def test_koriin_lisataan_kaksi_eri_tuotetta_ja_tilisiirto_kutsutaan_oikein(self):
        pankki_mock = Mock()
        viitegeneraattori = Mock()

        viitegeneraattori.uusi.return_value = 42

        varasto_mock = Mock()
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
        
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 3)
            
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 8)

    def test_koriin_lisataan_kaksi_samaa_tuotetta_ja_tilisiirto_kutsutaan_oikein(self):
        pankki_mock = Mock()
        viitegeneraattori = Mock()

        viitegeneraattori.uusi.return_value = 42

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 10)
    
    def test_koriin_lisataan_tuote_jota_on_tarpeeksi_ja_tuote_joka_on_loppu_ja_tilisiirto_kutsutaan_oikein(self):
        pankki_mock = Mock()
        viitegeneraattori = Mock()

        viitegeneraattori.uusi.return_value = 42

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 0
        
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 3)
            
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)


    def test_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        pankki_mock = Mock()
        viitegeneraattori = Mock()

        viitegeneraattori.uusi.return_value = 42

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)

        viitegeneraattori.uusi.return_value = 43

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("matti", "54321")

        pankki_mock.tilisiirto.assert_called_with("matti", 43, "54321", ANY, 10)
    
    def test_jokaiselle_maksutapahtumalle_pyydetaan_uusi_viitenumero(self):
        pankki_mock = Mock()
        viitegeneraattori = Mock()

        viitegeneraattori.uusi.side_effect = [42, 43, 44]

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("matti", "54321")

        pankki_mock.tilisiirto.assert_called_with("matti", 43, "54321", ANY, 5)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("liisa", "67890")

        pankki_mock.tilisiirto.assert_called_with("liisa", 44, "67890", ANY, 5)

    def test_korista_poistaminen_toimii(self):
        pankki_mock = Mock()
        viitegeneraattori = Mock()

        viitegeneraattori.uusi.return_value = 42

        varasto_mock = Mock()

        tuote = Tuote(1, "maito", 5)
        
        varasto_mock.saldo.return_value = 10
        varasto_mock.hae_tuote.return_value = tuote

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.poista_korista(1)

        varasto_mock.palauta_varastoon.assert_called_once_with(tuote)

    def test_lisataan_koriin_kun_varaston_saldo_nolla(self):
        pankki_mock = Mock()
        viitegeneraattori = Mock()

        viitegeneraattori.uusi.return_value = 42

        varasto_mock = Mock()

        varasto_mock.saldo.return_value = 0

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        
        self.assertEqual(len(kauppa._ostoskori._tuotteet), 0)
  
    def test_lisataan_koriin_kun_varaston_saldo_negatiivinen(self):
        pankki_mock = Mock()
        viitegeneraattori = Mock()

        viitegeneraattori.uusi.return_value = 42

        varasto_mock = Mock()

        varasto_mock.saldo.return_value = -5

        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        
        self.assertEqual(len(kauppa._ostoskori._tuotteet), 0)