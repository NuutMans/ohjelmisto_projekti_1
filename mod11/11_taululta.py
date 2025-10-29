class Elain:
    def __init__(self, nimi, syntymävuosi):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi

    def tulosta_tiedot(self):
        print(f"Eläimen nimi on: {self.nimi}, syntymävuosi: {self.syntymävuosi}")

    def ääntele(self, kerrat, ääni="jauuuuh"):
        for i in range(kerrat):
            print(ääni)

# perintä pythonissa merkatään suluilla. Muissa kielessä voi olla lisätty perään "Extend elain"
class Koira(Elain):
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.haukahdus = haukahdus
        super().__init__(nimi, syntymävuosi)
    #ylikirjoitetaan elaimen puhu()-metodi
    def puhu(self, kerrat, ääni="---"):
        self.hauku(kerrat)



    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Koiran nimi on: {self.nimi}, joka on syntynyt vuonna: {self.syntymävuosi}")

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return

class Kissa(Elain):
    def __init__(self, nimi, syntymävuosi):
        super().__init__(nimi, syntymävuosi)

    def puhu(self, kerrat, ääni="---"):
        super().puhu(kerrat, "Miumau")

elaimet = []
elaimet.append(Koira("Ruffe", 2017))
elaimet.append(Kissa("Maukku", 2016))
elaimet.append(Elain("Tipu", 2023))

for elain in elaimet:
    elain.tulosta_tiedot()
