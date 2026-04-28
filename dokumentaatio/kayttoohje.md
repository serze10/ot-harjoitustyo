
# Käyttöohje (alustava)

## Yleistä

Projektin tarkoitus on lukea FASTA-muotoisia sekvenssejä, suorittaa DNA-analyysiä (pituus, nukleotidilaskenta, GC-prosentti, GC-profiili) sekä etsiä käyttäjän määrittämiä motifteja. Sovellus tarjoaa sekä graafisen käyttöliittymän että komentorivikäytön.

## Graafinen käyttöliittymä (GUI)

1. Käynnistä GUI-replikaatio suoraan Pythonilla:

   ```bash
   poetry run invoke start
   ```

2. Päätoiminnot GUI:ssa:
   - "Open FASTA": valitse FASTA-tiedosto (.fasta) sisältäen yhden tai useamman sekvenssin.
   - Valitse haluamasi sekvenssi valikosta (jos tiedostossa on useampi sekvenssi).
   - Aseta GC-profiilin parametrit (ikkuna ja step) tarvittaessa ja valitse "Compute GC" tai käynnistä koko analyysi "Run" -painikkeella.
   - Motifin etsimiseksi kirjoita motiivi kenttään (esim. `ATG`) ja paina "Find Motif" — tuloksena näytetään esiintymäindeksit (0-pohjainen).
   - Tulokset voi tallentaa "Save Result" -painikkeella JSON- tai CSV-muotoon, tallennusikkuna kysyy tiedostonimen.

## Komentorivikäyttö (CLI)

1. Voit ajaa yksittäisen tiedoston/analyysin komentoriviltä:

   ```bash
   python3 src/run_dna.py --help
   ```

   `run_dna.py` tarjoaa valinnat GC-profiilin laskemiseen, tallennukseen ja muihin asetuksiin. Ajettaessa suoraan repositorion juuressa, käytä `python3 src/run_dna.py` ja anna tiedosto- ja parametritiedot komentorivillä.

## Testaus

- Testit sijaitsevat `tests/`-hakemistossa. Suositut tavat ajaa testit:

  ```bash
  poetry run invoke test

  # tai suoraan pytest
  python3 -m pytest -q
  ```
