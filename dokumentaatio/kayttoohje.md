# Käyttöohje

## Pelin asennus

Lataa [viimeisin julkaisu](https://github.com/Robomarti/harjoitustyo/releases/latest).

- Asenna riippuvuudet komennolla 
```bash
poetry install
```

- Käynnistä sovellus komennolla 
```bash
poetry run invoke start
```

## Pelin pelaaminen
Pelin idea on liikkua vastustajan takana olevalle lipulle, siepata se, ja liikkua takaisin omalle maalille ilman, että vastustaja osuu sinuun ammuksellaan. Pelissä liikutaan nuolinäppäimillä, ja vuoroa vaihdetaan välilyönnistä. Pelaaja numero 2:den vuoron jälkeen on "vuoro 3" jolloin ammukset liikkuvat (ja pelaajat kun olen saanut sen toimimaan).
Sen voi teknillisesti ohittaa painamalla välilyöntiä heti, mutta silloin ammukset eivät osu pelaajiin. 

Ammuksia ammutaan klikkaamalla hiirellä siihen kohtaan ruutua, johon oletat
vastustajasi liikkuvan. Pelaajilla on vain yksi ammus, joten uuden kohdan klikkaaminen ei luo uutta ammusta, vaan vaihtaa oman ammuksen suuntaa.

Pelaaja saa yhden pisteen osuessaan vastustajansa ammuksellaan, sekä viisi pistettä viedessään vastustajan lipun omaan maaliinsa. Pelaajat voivat käyttää maaleja esteinä heidän ja vastustajan ammusten välillä.

Viedessään vastustajan lipun omaan maaliinsa, pelaaja ei liiku näytöllä, mutta hänen liikkumisensa on vuoron osalta käytetty.

Pelaajat ei normaalisti voi liikkua oman lippunsa päältä, ettei omaa lippua voi vartioida liian tiukasti. Jos oma lippu on pudonnut samaan kohtaan mihin synnyt kun olet kuollut, niin tämä todennäköisesti poistaa lipun koko pelistä.

Pelaajat voivat olla sisäkkäin, jos he molemmat liikkuvat samaan ruutuun. Tällöin vain toisen pelaajan grafiikka näkyy pelaajille. Tämän ei pitäisi muuttaa peliä mitenkään.

Pelaajien nimet ja pelin ulkonäköä ja pituutta voi muokata "services" -hakemiston "settings.py" -tiedoston kautta. Huomaathan että virheellisten muokkausten suorittaminen voi aiheuttaa pelin kaatumisen, eikä tiedoston oikeellisuudelle ole testiä tällä hetkellä.
