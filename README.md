# Capture The Flag

Pelin idea on liikkua vastustajan takana olevalle lipulle, siepata se, ja liikkua takaisin omalle maalille ilman, että vastustaja osuu sinuun ammuksellaan. Pelissä liikutaan nuolinäppäimillä, ja vuoroa vaihdetaan välilyönnistä. Pelaaja numero 2:den vuoron jälkeen on "vuoro 3" jolloin ammukset liikkuvat (ja pelaajat kun olen saanut sen toimimaan).
Sen voi ohittaa painamalla välilyöntiä heti.

## Pelin asennus

- Asenna riippuvuudet komennolla 
```bash
poetry install
```

- Käynnistä sovellus komennolla 
```bash
poetry run invoke start
```

## Muut komennot

- Ohjelmaa voi testata komennolla
```bash
poetry run invoke test
```

- Testikattavuusraportin voi generoida komennolla
```bash
poetry run invoke coverage-report
```
Raportti generoituu hakemistoon nimeltä htmlcov

- Ohjelman pylint-tarkistukset voi suorittaa komennolla
```bash
poetry run invoke lint
```

## Viikko 5 release:
[](https://github.com/Robomarti/harjoitustyo/releases/tag/viikko5)

## Dokumentaatio:

- [Vaatimusmäärittely](https://github.com/Robomarti/harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [Työaikakirjanpito](https://github.com/Robomarti/harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

- [Changelog](https://github.com/Robomarti/harjoitustyo/blob/master/dokumentaatio/changelog.md)

- [Arkkitehtuuri](https://github.com/Robomarti/harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)