# DNA-analyysityökalu


## Dokumentaatio

Vaatimusmäärittely: [dokumentaatio/vaatimusmaarittely.md](dokumentaatio/vaatimusmaarittely.md)

Tuntikirjanpito: [Tuntikirjanpito](https://github.com/serze10/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

Changelog: [Changelog](dokumentaatio/changelog.md)

Arkkitehtuuri: [Arkkitehtuuri] (https://github.com/serze10/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

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
