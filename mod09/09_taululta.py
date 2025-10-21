# instanssi = ilmentymä = olio
# luokka ja olio ovat tärkeimmät käsitteet mitä täytyy ymmärtää

# luokka määritellään isolla alkukirjaimella (ohjelmointikäytäntö)
# __init__ on konstruktori (alustaja) -metodi ajetaan kun luokasta luodaan
# nimenomaan metodi tai toiminto, eikä funktio, koska se on luokan alla # (self) viittaa siihen olioon itseensä. Se on vain tapa mitä
class Koira:
    count = 0
    def __init__(self, name, weight=0):
        print(f"uusi koiraolio ({name}) luotu.")
        self.name = name
        self.weight = weight
        Koira.count = Koira.count + 1
    # luokan toiminto eli metodi (verrattavissa funktio)
    # tämä on funktiokoiraluokan metodi, suomeksi toiminto. Mitä koira pystyy tekemään. Koira pystyy haukkumaan
    # metodi ton luokan sisällä määritettyjä toimintoja, joita voi kutsua muualta koodista
    def hauku(self, toWhom, times=1):
        print(f"{self.name} HAUKKUU {toWhom}")
        for i in range(times):
            if self.weight < 10:
                print("Wufwuf")
            else:
                print("Hauuuu")
# pisteen jälkene voi tulla vaikka koira1.name koira1.birthday koira1.weight
koira1 = Koira("Rekku", 7) #ensimmäisen muuttujan kautta pääsee tähän käsiksi
koira2 = Koira("Matti", 26) # voi luoda toisen identtisen koiran JA muuttujan kautta pääsee tähän käsiksi
koira1.hauku("Matille")
koira2.hauku("Rekulle", 5)
print(f"Koiraoliota on luotu yhteensä {Koira.count} kpl.")


#koira3 = koira1 # kaksi saman luokan ilmentymää (oliota)
#koira2.name = "Ruffe"
#print(koira1.name)
#print(koira2.name)
#print(koira3.name)
