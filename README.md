# DNA-analyysityökalu


## Dokumentaatio

Vaatimusmäärittely: [dokumentaatio/vaatimusmaarittely.md](dokumentaatio/vaatimusmaarittely.md)

Tuntikirjanpito: [Tuntikirjanpito](https://github.com/serze10/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

Changelog: [Changelog](dokumentaatio/changelog.md)

## Asennus

Asenna riippuvuudet:

```bash
poetry install
```

Käynnistä sovellus:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

Suorita sovellus:
(suorittaa tällä hetkellä testi datalla suoraan tämän hetkisen toiminnon)
```bash
poetry run invoke start
```

Testaus:

```bash
poetry run invoke test
```

Testikattavuus (HTML-raportti):

```bash
poetry run invoke coverage-report
```

Raportti generoituu `htmlcov`-hakemistoon.

Pylint (staattinen analyysi):

```bash
poetry run invoke pylint
```

Suorita CLI ja tallenna tulokset JSON/CSV:

```bash
# Tallenna JSON-muotoon
poetry run invoke run-json

# Tallenna CSV-muotoon
poetry run invoke run-csv
```

Voit myös ajaa suoraan skriptin ilman invokea:

```bash
python3 src/run_dna.py src/testfasta/testi.fasta --gc-profile --save-results out.json
python3 src/run_dna.py src/testfasta/testi.fasta --gc-profile --save-results out.csv
```

