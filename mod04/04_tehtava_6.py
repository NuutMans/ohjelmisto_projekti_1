
# mod04 tehtävä 6
import random
# Kaikkien pisteiden määrä N
N = 10 # kysy käyttäjän laittamaan arvon.
# ympyrän sisään osuvien pisteiden lkm n
i = 0
while i > N:
        i = i + 1
        # arvotaan random/satunnainen piste koordinaatistoon (x, y)
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        print(f"Arvottu piste: {x}, {y}")

        # todo: testaa, toteuttaako piste epäyhtälön x^2+y^2<1
        # jos ehto on totta, kasvata n-laskurin arvoa  --käytä if-lausetta
        # while userinput != ""  -- tarkistaa onko erisuuri (mitä tahansa muuta kuin) tyhjä merkkijono

    #todo: laske ja tulosta piin likiarvo käyttäen kaavaa: π≈4n/N
