# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä
# vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat
# vuodenajat merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden
# mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.



vuodenajat = (
    "talvi", # tammikuu
    "talvi", # helmikuu
    "kevät", # maaliskuu
    "kevät", # huhtikuu
    "kevät",
    "kesä",
    "kesä",
    "kesä",
    "syksy",
    "syksy",
    "syksy",
    "talvi", #joulukuu
)

kuukauden_numero = int(input("Anna kuukauden numero (1-12): "))
if 1 <= kuukauden_numero <= 12:
    print(vuodenajat[kuukauden_numero-1])






