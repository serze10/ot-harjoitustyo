# DNA-analyysityökalu


## Dokumentaatio

Vaatimusmäärittely: [Vaatimusmaarittely](dokumentaatio/vaatimusmaarittely.md)

Tuntikirjanpito: [Tuntikirjanpito](dokumentaatio/tyoaikakirjanpito.md)

Changelog: [Changelog](dokumentaatio/changelog.md)

Arkkitehtuuri: [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

Käyttöohje: [Käyttöohje](dokumentaatio/kayttoohje.md)

Release: [Release](ot-harjoitustyo/releases)

## Asennus

Asenna riippuvuudet:

```bash
poetry install
```

Käynnistä sovellus (avautuu graafinen käyttöliittymä):

```bash
poetry run invoke start
```

## Komentorivitoiminnot

Suorita sovellus (avautuu graafinen käyttöliittymä):

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
