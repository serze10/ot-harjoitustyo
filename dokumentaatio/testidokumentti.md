# Testidokumentti

Tämä dokumentti kuvaa projektin testikäytännöt, testien ajotavat ja ohjeet uusien testien kirjoittamiseen.

## Yleiskuva

- Testit sijaitsevat pääosin `src/`-kansion alla olevissa testitiedostoissa.
- Projektissa käytetään `pytest`-testikehystä.

## Kuinka ajetaan testit

- Aja kaikki testit (poetry + invoke -komennot on määritelty README:ssa):

```bash
poetry run invoke test
```

- Generoi kattavuusraportti (HTML):

```bash
poetry run invoke coverage-report
# raportti löytyy hakemistosta htmlcov/
```

- Staattinen analyysi (pylint):

```bash
poetry run invoke pylint
```

## GUI-testit

- GUI-komponentteja (Tkinter) testattaessa suositellaan dialogien ja tiedostonvalintojen mockaamista.
- Testit voivat korvata `filedialog`- ja `messagebox`-kutsut `unittest.mock`-kirjastolla.

Esimerkki: korvaa `filedialog.askopenfilename` testausta varten.

## Yksikkötestit

- Yksikkötestit keskittyvät pieniin, eristettyihin funktioihin (esim. `parser`, `analysis`).
- Sijoita yksikkötestit lähelle testattavaa moduulia tai `src/tests/`-kansioon.
- Testaa sekä normaali- että virhepolut (tyhjät sekvenssit, erikoismerkit, virheelliset tiedostot).
- Pidä testit pieninä ja idempotentteina; vältä verkko- tai järjestelmäsidonnaisuuksia.

## Kirjoitusohjeet uusille testeille

- Lisää testit samaan hakemistoon kuin testattava moduuli tai projektiin `tests/`-kansioon, riippuen testityypistä.
- Käytä selkeitä fixtureja toistuvien tilanteiden valmisteluun.
- Testaa sekä normaali- että virhepolut (esim. virheellinen FASTA-tiedosto).

## Kattavuus ja vaatimukset

- Pyri kirjoittamaan testit, jotka kattavat ydintoiminnot: parser, analyysi ja tallennus.
- Määrittele projektille haluttu kattavuustaso (esim. 80%) ja lisää se tarvittaessa CI-putkeen.

## Järjestelmätestaus ja tunnetut laatuongelmat

Järjestelmätestauksen tarkoituksena on varmistaa sovelluksen end-to-end -toiminta käyttöliittymän ja komentorivin kautta. Manuaaliset järjestelmätestit voivat sisältää:

- Avaus ja lukeminen eri FASTA-tiedostoilla (yksi sekvenssi / useita sekvenssejä).
- Komentorivikäyttö: `run_dna.main()` eri argumenttivariaatioilla (GC-profiili päälle/pois, tallennuspolku).
- GUI-polut: tiedoston avaaminen, sekvenssin valitseminen, analyysin suoritus, motif-haku ja tulosten tallennus.

Tunnetut laatuongelmat ja rajoitteet (projektissa havaitut):

- Testikattavuus: nykyinen testikattavuus `src`-kansiossa on ~77% (raportti ajettiin `coverage`-työkalulla `tests/`-hakemistolla). Joitain analyysi- ja GUI-polkuja ei ole täysin katettu.

Manuaalinen järjestelmätestausohje (lyhyt):

1. Käynnistä GUI: `poetry run invoke start` ja avaa `src/testfasta/testi.fasta` tiedosto.
2. Valitse sekvenssi, suorita analyysi oletusarvoisilla asetuksilla ja tarkista, että pituus, nukleotidilaskenta ja GC-prosentti vastaavat odotuksia.
3. Syötä motif ja varmista, että kaikki esiintymät näkyvät tekstialueella.
4. Tallenna tulokset JSON- ja CSV-muotoon ja varmista, että tiedostot avautuvat ja sisältävät odotetut kentät.



---