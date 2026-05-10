# DNA‑ANALYYSITYÖKALU – VAATIMUSMÄÄRITTELY

## 1. Sovelluksen yleiskuvaus

DNA‑analyysityökalu on sovellus, jonka avulla käyttäjä voi tarkastella ja analysoida DNA‑sekvenssejä FASTA‑tiedostoista. Sovellus laskee sekvenssistä yleisiä perusanalyysimittareita (pituus, nukleotidien frekvenssit, GC‑pitoisuus) ja etsii yksinkertaisia motiiveja. Sovellus on tarkoitettu pienimuotoiseen oppimiskäyttöön ja kurssiharjoitteluun, ei tieteellisen tason bioinformatiikkaan.

Sovellusta voidaan käyttää komentoriviltä tai graafisen käyttöliittymän kautta.

---

## 2. Käyttäjät

Sovelluksella on yksi käyttäjärooli:

- **Käyttäjä:** henkilö, joka haluaa ladata DNA‑sekvenssin ja tarkastella sen perusominaisuuksia. Sovellus ei sisällä kirjautumista eikä eri käyttöoikeustasoja.

---

## 3. Toiminnallisuudet

Vaatimukset on jaoteltu kurssin ohjeen mukaisesti.

### 3.1 Perusversion toiminnallisuudet

####  Tiedoston käsittely
- Käyttäjä voi valita FASTA‑tiedoston analysoitavaksi. Done
- Sovellus osaa lukea yhden tai useita sekvenssejä sisältävän FASTA‑tiedoston. Done
- Käyttäjä voi valita, mitä tiedoston sekvenssiä analysoidaan. Done

####  Sekvenssin tarkistus
- Sovellus tarkistaa, että sekvenssi sisältää vain sallitut nukleotidimerkit: **A, C, G, T, N**. Done
- Virheellisistä merkeistä ilmoitetaan käyttäjälle. Done

####  Perusanalyysi
- Sekvenssin kokonaispituus.  Done
- Nukleotidien lukumäärät (A/C/G/T).  Done
- GC‑pitoisuus (%).  Done
- GC‑pitoisuuden liukuva ikkuna (esim. window = 100, step = 50).  Done

####  Motiivien etsiminen
- Käyttäjä voi syöttää motiivin (esim. "ATG"). Done
- Sovellus etsii kaikki motiivin esiintymiskohdat sekvenssistä. Done

####  Käyttöliittymä
- Sovellusta voidaan käyttää komentoriviltä. Done
- Vaihtoehtoisesti voidaan toteuttaa yksinkertainen Tkinter‑käyttöliittymä Done

---

### 3.2 Jatkokehitysideat (laajennettavat toiminnallisuudet)

####  Visualisoinnit
- GC‑pitoisuuden liukuva ikkuna (esim. window = 100, step = 50). 
- GC‑profiilin kuvaaja (matplotlib).
- k‑mer‑tilastojen pylväsdiagrammi.

####  k‑mer‑tilastot
- Käyttäjä voi valita k‑merin pituuden (esim. k = 1–10).
- Sovellus laskee sekvenssin yleisimmät k‑merit.
- Sovellus näyttää vähintään **top‑10** k‑meriä.

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