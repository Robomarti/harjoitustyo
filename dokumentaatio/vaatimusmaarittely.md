# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on olla pieni kaksinpelattava peli, jossa pelaajat yrittävät vallata toistensa liput ja kuljettaa sen omaan maaliinsa.


## Suunnitellut toiminnallisuudet
  
### Pelin ulkonäkö

- Peli toteutetaan 2d:nä, ja sitä pelataan ylhäältä katsotusta kuvakulmasta.
![](./kuvat/pelin-hahmotelma.png)

### Pelin pelaaminen

- Peliä pelataan vuorotellen samalla tietokoneella, pelaaja 1 aloittaa.
- Vuorot pelataan salassa, esimerkiksi kääntämällä näytön poispäin toisesta pelaajasta.
- Aika on "pysähtynyt" vuorojen aikana, ja molempien pelaajien toiminnot tapahtuvat samaan aikaan, kun pelaaja 2 on lopettanut vuoronsa.
- Vuoronsa aikana pelaajalla on kaksi mahdollista toimintoa: liikkuminen ja hyökkääminen.
  - Pelaaja voi tehdä molemmat toiminnot missä järjestyksessä tahansa.
  - Liikkuessaan pelaaja voi liikkua tietyn etäisyyden haluamaansa suuntaan.
    - Jos pelaaja liikkuu vastakkaisen pelaajan lipun päälle, hän alkaa kantamaan sitä mukanansa.
    - Jos pelaaja liikkuu vastakkaisen pelaajan lipun kanssa omaan maaliinsa, hän saa viisi pistettä.
  - Hyökätessään pelaaja voi ampua haluamaansa suuntaan.
    - Jos pelaaja osuu toiseen pelaajaan, hän saa yhden pisteen, ja pelaaja johon hän osui palaa takaisin kohtaan, josta hän aloitti pelin.
      - Jos osuttu pelaaja oli kantamassa toisen pelaajan lippua, lippu jää siihen kohtaan mihin hän "kuoli".
- Molemmilla pelaajilla on käytettävänään 30 vuoroa ennen kuin peli päättyy.
  
### Pelin päätös

  - Pelaajien pisteitä verrataan keskenään, ja voittaja ilmoitetaan.
  - Pelaajille näytetään "Pelaa uudestaan" näyttö. 

## Extraominaisuudet

- Koko pelin pituutta voi vaihtaa settings.py tiedoston asetuksia.
- Pelin ulkonäköä voi muuttaa vaihtamalla settings.py tiedoston asetuksia.
- Pelaajat voivat valita itselleen nimet vaihtamalla settings.py tiedoston asetuksia.


## Jatkokehitysideoita

Perusversion jälkeen peliin lisätään seuraavat toiminnallisuudet ajan salliessa:
- Pelaajien pisteitä voi verrata ennätyspistemäärään, ja ennätyspisteet voidaan tallettaa tietokantaan.
- Pelaajia voi olla useampi kuin 2.
- Pelin voi tallentaa jokaisen vuoron jälkeen, ja siihen voi palata myöhemmin.
