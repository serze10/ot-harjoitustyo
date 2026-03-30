# DNA-analyysityökalu


## Dokumentaatio

Vaatimusmäärittely: [dokumentaatio/vaatimusmaarittely.md](dokumentaatio/vaatimusmaarittely.md)

Linkki: [Tuntikirjanpito](https://github.com/serze10/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

Lisätietoja muutoksista: [Changelog](dokumentaatio/changelog.md)

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

- Suorita sovellus:

```bash
poetry run invoke start
```

- Testaus:

```bash
poetry run invoke test
```

- Testikattavuus (HTML-raportti):

```bash
poetry run invoke coverage-report
```

Raportti generoituu `htmlcov`-hakemistoon.

- Pylint (staattinen analyysi):

```bash
poetry run invoke lint
```

