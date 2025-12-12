class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros  # hissi alkaa aina alimmasta kerroksesta

    def kerros_alas(self):
        if self.kerros == self.alin_kerros:
            print("PÄÄSIT ALIMPAAN KERROKSEEN")
        else:
            self.kerros -= 1
            print(f"Olet nyt kerroksessa {self.kerros}")

    def kerros_ylös(self):
        if self.kerros == self.ylin_kerros:
            print("PÄÄSIT YLIMPÄÄN KERROKSEEN")
        else:
            self.kerros += 1
            print(f"Olet nyt kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, kohde_kerros):
        kohde_kerros = int(kohde_kerros)

        if kohde_kerros > self.kerros:
            for _ in range(self.kerros, kohde_kerros):
                self.kerros_ylös()

        elif kohde_kerros < self.kerros:
            for _ in range(self.kerros, kohde_kerros, -1):
                self.kerros_alas()



hissi1 = Hissi(0, 7)

hissi1.siirry_kerrokseen(5)
hissi1.siirry_kerrokseen(0)