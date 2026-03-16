# DNA‑ANALYYSITYÖKALU – VAATIMUSMÄÄRITTELY

## 1. Sovelluksen yleiskuvaus

DNA‑analyysityökalu on sovellus, jonka avulla käyttäjä voi tarkastella ja analysoida DNA‑sekvenssejä FASTA‑tiedostoista. Sovellus laskee sekvenssistä yleisiä perusanalyysimittareita (pituus, nukleotidien frekvenssit, GC‑pitoisuus), etsii yksinkertaisia motiiveja ja tuottaa k‑mer‑tilastoja. Sovellus on tarkoitettu pienimuotoiseen oppimiskäyttöön ja kurssiharjoitteluun, ei tieteellisen tason bioinformatiikkaan.

Sovellusta voidaan käyttää komentoriviltä tai graafisen käyttöliittymän kautta. Perusversion toiminnallisuus ei edellytä käyttöliittymää, mutta se voidaan toteuttaa myöhemmässä vaiheessa.

---

## 2. Käyttäjät

Sovelluksella on yksi käyttäjärooli:

- **Käyttäjä:** henkilö, joka haluaa ladata DNA‑sekvenssin ja tarkastella sen perusominaisuuksia. Sovellus ei sisällä kirjautumista eikä eri käyttöoikeustasoja.

---

## 3. Toiminnallisuudet

Vaatimukset on jaoteltu kurssin ohjeen mukaisesti.

### 3.1 Perusversion toiminnallisuudet

####  Tiedoston käsittely
- Käyttäjä voi valita FASTA‑tiedoston analysoitavaksi.
- Sovellus osaa lukea yhden tai useita sekvenssejä sisältävän FASTA‑tiedoston.
- Käyttäjä voi valita, mitä tiedoston sekvenssiä analysoidaan.

####  Sekvenssin tarkistus
- Sovellus tarkistaa, että sekvenssi sisältää vain sallitut nukleotidimerkit: **A, C, G, T, N**.
- Virheellisistä merkeistä ilmoitetaan käyttäjälle.

####  Perusanalyysi
- Sekvenssin kokonaispituus.
- Nukleotidien lukumäärät (A/C/G/T).
- GC‑pitoisuus (%).

####  k‑mer‑tilastot
- Käyttäjä voi valita k‑merin pituuden (esim. k = 1–10).
- Sovellus laskee sekvenssin yleisimmät k‑merit.
- Sovellus näyttää vähintään **top‑10** k‑meriä.

####  Motiivien etsiminen
- Käyttäjä voi syöttää motiivin (esim. "ATG").
- Sovellus etsii kaikki motiivin esiintymiskohdat sekvenssistä.

####  Käyttöliittymä
- Sovellusta voidaan käyttää komentoriviltä.
- Vaihtoehtoisesti voidaan toteuttaa yksinkertainen Tkinter‑käyttöliittymä (ei pakollinen perusversiossa).

---

### 3.2 Jatkokehitysideat (laajennettavat toiminnallisuudet)

####  Visualisoinnit
- GC‑pitoisuuden liukuva ikkuna (esim. window = 100, step = 50).
- GC‑profiilin kuvaaja (matplotlib).
- k‑mer‑tilastojen pylväsdiagrammi.

####  Edistyneet analyysit
- ORF‑etsintä (Open Reading Frame).
- Käänteinen komplementti ja toisen DNA‑säikeen analyysi.
- DNA → aminohappo ‑translaatio.

####  Käyttöliittymä
- Täysin graafinen käyttöliittymä Tkinterillä.
- Välilehtiin jaettu näkymä:  
  *Yhteenveto / k‑merit / GC‑profiili / Motiivit.*

####  Tiedon tallennus
- Analyysitulosten tallentaminen CSV‑ tai JSON‑tiedostoon.
- Kuvioiden tallennus PNG‑muotoon.

####  Suorituskyky
- Suurten FASTA‑tiedostojen lukeminen stream‑pohjaisesti.
- Optimoidut k‑mer‑laskut (esim. numpy).

---

## 4. Toimintaympäristö ja tekniset rajoitteet

- Sovelluksen tulee toimia **Python 3.12** ‑ympäristössä.
- Sovellus tulee toimia **Linux-, macOS- ja Windows‑käyttöjärjestelmissä**.
- Graafinen käyttöliittymä (jos toteutetaan) käyttää Pythonin **Tkinter**‑kirjastoa.
- Visualisointeihin voidaan käyttää **matplotlib**‑kirjastoa.
- Syötedata luetaan käyttäjän paikalliselta levyltä.

---