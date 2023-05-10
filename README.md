# Capture The Flag

Pelin idea on liikkua vastustajan takana olevalle lipulle, siepata se, ja liikkua takaisin omalle maalille ilman, että vastustaja osuu sinuun ammuksellaan. Pelissä liikutaan nuolinäppäimillä, ja vuoroa vaihdetaan välilyönnistä. Pelaaja numero 2:den vuoron jälkeen on "vuoro 3" jolloin ammukset liikkuvat (ja pelaajat kun olen saanut sen toimimaan).
Sen voi teknillisesti ohittaa painamalla välilyöntiä heti, mutta silloin ammukset eivät osu pelaajiin. Ammuksia ammutaan klikkaamalla hiirellä siihen kohtaan ruutua, johon oletat
vastustajasi liikkuvan. Pelaajilla on vain yksi ammus, joten uuden kohdan klikkaaminen ei luo uutta ammusta, vaan vaihtaa oman ammuksen suuntaa.

## Dokumentaatio:

- [Käyttöohje](https://github.com/Robomarti/harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

- [Vaatimusmäärittely](https://github.com/Robomarti/harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [Työaikakirjanpito](https://github.com/Robomarti/harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

- [Changelog](https://github.com/Robomarti/harjoitustyo/blob/master/dokumentaatio/changelog.md)

- [Arkkitehtuuri](https://github.com/Robomarti/harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

- [Testausdokumentti](https://github.com/Robomarti/harjoitustyo/blob/master/dokumentaatio/testaus.md)

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
Komento tekee samalla raporttiin vaaditut testit. Raportti generoituu hakemistoon nimeltä htmlcov.

- Ohjelman pylint-tarkistukset voi suorittaa komennolla
```bash
poetry run invoke lint
```

## Viikko 5 release:
[Löytyy täältä](https://github.com/Robomarti/harjoitustyo/releases/tag/viikko5)

## Viikko 6 release:
[Löytyy täältä](https://github.com/Robomarti/harjoitustyo/releases/tag/viikko6)

## Viikko 7 release:
[Löytyy täältä](https://github.com/Robomarti/harjoitustyo/releases/tag/viikko7)