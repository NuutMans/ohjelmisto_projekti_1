class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0


# Ohjelma
auto = Auto("ABC-123", 142)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print("Auton nopeus kiihdytysten jälkeen:", auto.nopeus, "km/h")

auto.kiihdyta(-200)
print("Auton nopeus hätäjarrutuksen jälkeen:", auto.nopeus, "km/h")
