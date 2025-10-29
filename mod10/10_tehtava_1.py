class Hissi:
    def __init__(self, alin_kerros, ylin_kerros, kerros=0):
        self.kerros = kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    # laskee/vähentää kerrosnumeroa niin kauan kunnes kerros on laskenut kerrokseen asti. ei mene sitä alemmas
    def kerros_alas(self):
        if self.kerros == self.alin_kerros:
            print("PÄÄSIT ALIMPAAN KERROKSEEN")
        else:
            self.kerros = self.kerros - 1
            print(f"olet nyt kerroksessa {self.kerros}" )




    # kasvattaa/nostaa kerrosnumeroa niin kauan kunnes kerros on kohdekerros saavutettu. ei mene sitä ylemmäs
    def kerros_ylös(self):
        if self.kerros == self.ylin_kerros:
            print("PÄÄSIT YLIMPÄÄN KERROKSEEN")
        else:
            self.kerros = self.kerros + 1
            print(f"olet nyt kerroksessa {self.kerros}" )




    def siirry_kerrokseen(self, kohde_kerros):
        pass
# tee yksi for-loop joka vertaa kohde_kerrosta nykysen kerroksen. Eli nostaa hissin tämänhetkistä kerrosnumeroa ylös
# jos se on suurempi kuin nykyinen kerros niin kauan kunnes saavuttaa kohdekerookseen
# Sama for-loop vertaa kerrosta nykyiseen kerrokseen, ja laskee sitä jos kohdekerros on pienempi kuin nykyinen kerros,
# kunnes saavuttaa kohdekerroksen
# alin ja ylin kerros tarkistetaan jo kerros_alas ja kerros_ylös funktioissa joten tässä ei tarvitse tehdä sitä.
# Pitää vain kutsua niitä.

hissi1 = Hissi(0, 7)

hissi1.kerros_alas()
hissi1.kerros_ylös()
hissi1.kerros_ylös()
hissi1.kerros_ylös()
hissi1.kerros_ylös()




'''kohde_kerros = input("Mihin kerrokseen haluat mennä?\nKirjoita kerroksen numero: ")
hissi1.siirry_kerrokseen(kohde_kerros)
'''

'''
siirry_kerrokseen katsoo tämän hetkisen kerroksen ja vertaa sitä siihen mihin kerrokseen haluat 
matkustaa(input(henkilö painaa nappia(kirjoittaa kerroksen numeron))) ja 
onko se isompi vai pienempi kuin tämänhetkinen_kerros. 
'''
