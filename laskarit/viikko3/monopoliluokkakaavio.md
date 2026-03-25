classDiagram
    %% PELIN PERUSRAKENNE
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelaaja "2..8" -- "1" Monopolipeli
    Pelinappula "1" -- "1" Pelaaja
    Ruutu "1" -- "0..8" Pelinappula

    %% PELILAUTA JA RUUDUT
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava

    %% ERITYISRUUDUT
    Ruutu <|-- Aloitusruutu
    Ruutu <|-- Vankila
    Ruutu <|-- Sattuma
    Ruutu <|-- Yhteismaa
    Ruutu <|-- Asema
    Ruutu <|-- Laitos
    Ruutu <|-- Katu

    %% PELILAUDAN ON TUNNETTAVA START JA JAIL
    Pelilauta "1" -- "1" Aloitusruutu : start
    Pelilauta "1" -- "1" Vankila : jail

    %% TOIMINNOT
    Ruutu "1" -- "1" Toiminto
    Kortti "1" -- "1" Toiminto

    %% KORTIT
    Sattuma "1" -- "*" Kortti
    Yhteismaa "1" -- "*" Kortti

    %% KATUJEN LISÄOMINAISUUDET
    Katu "1" -- "0..1" Pelaaja : omistaja
    class Katu {
        +nimi
        +talot (0..4)
        +hotelli (0..1)
    }

    %% PELAAJAN RAHAT
    class Pelaaja {
        +raha
    }