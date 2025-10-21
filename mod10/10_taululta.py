class Yritys:
    def __init__(self, nimi, osoite):
        self.nimi = nimi
        self.osoite = osoite
        self.hoitolat = []

    def lisää_hoitola(self, nimi):
        self.hoitolat.append(nimi)

    def tulosta_hoitola(self):
        for h in self.hoitolat:
            print(h.nimi)

    def anna_joululahja(self):
        print("yritys antaa joululahjan jokaiselle koiralle 🐶🎁")

        # tapa 1: iteroidaan kaikki läpi
        for h in self.hoitolat:
            print(f"Annetaan lahjoja {h.nimi} koirille: ")
            for koira in h.koira_lista:
                print(f"{koira.nimi} saa joululahjaksi luun!")
                koira.hauku(1)


        # tapa 2: käytetään metodeja
        for hoitola in hoitolat:
            print("yritys antaa toisen luun")
            hoitola.tervehdi_koiria(1)


# luodaan pysyvä assosisaatiosuhde Hoitola ja Koira-luokkien välillä
# Koira tallennetaan luokan ominaisuutena olevaan koiralistaan

class Hoitola: # konstruktori määrittelee jokaisen luokan yhteiset ominaisuudet tai arvot
    def __init__(self, nimi):
        self.nimi = nimi
        self.koira_lista = []

    # metodi, jonka parametrina annetaan viittaus Koira olioon
    # assosisaatiosuhde on voimassa vain metodikutsun ajan
    def koira_sisään(self, koira):
        print(koira)
        print(f"lisätään koira {koira.nimi} sisään hoitolaan")
        self.koira_lista.append(koira)
        # kutsutaan olion sisäkkäistä / omaa metodia
        self.printtaa_koirat()
        return

    def koira_ulos(self, koira):
        print("hyvästellään koirat")
        self.koira_lista.remove(koira)
        print(f"👋 Moikka {koira.nimi}")
        return

    def printtaa_koirat(self):
        print(f"hoitolassa {self.nimi} on seuraavat koirat")
        for koira in self.koira_lista:
            print(koira.nimi)

    def tervehdi_koiria(self, kerrat):
        print(f"Tervehditään koiria ja jokainen koira haukkuu iloisesti: ")
        for koira in self.koira_lista:
            koira.hauku(kerrat)



class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return


# pääohjelma
# 4 eri koiraa

koira1 = Koira("Jussi", 2014, "Hau-hau")
koira2 = Koira("Kalle", 2025, "WOOF WOOF")
koira3 = Koira("Lukki", 2010, "JAUH JAUH")
koira4 = Koira("Ali", 2004, "Haaaw Haaw")

print(koira1.nimi)
koira1.hauku(1)
koira4.hauku(2)

# luodaan eri hoitolat
tassuhoitola = Hoitola("Tassuhoitola")
karvakamut = Hoitola("Karvakamut")

# lisätään koiria koirahoitolaan
# koira1 ja koira2 laitetaan Tassuhoitolaan
tassuhoitola.koira_sisään(koira1)
tassuhoitola.koira_sisään(koira2)

# lisätään koira3 ja koira 4 hoitolaan 2
karvakamut.koira_sisään(koira3)
karvakamut.koira_sisään(koira4)

# listataan hoitolaan sisälletyt koirat
tassuhoitola.printtaa_koirat()
karvakamut.printtaa_koirat()

# tervehditään koiria
print()
tassuhoitola.tervehdi_koiria(2)

# koira lähtee hoitolasta
print()
tassuhoitola.koira_ulos(koira1)

# luodaan yritys
yritys = Yritys("Koira Mafia", "Osoitekuja 12")

# lisätään yritykseen hoitolat
yritys.lisää_hoitola(tassuhoitola)
yritys.lisää_hoitola(karvakamut)

yritys.tulosta_hoitola()

yritys.anna_joululahja()

