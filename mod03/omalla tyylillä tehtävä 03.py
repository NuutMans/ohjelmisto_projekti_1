# mod03 tehtävät

# tehtävä 1, kuhan pituus, päästä vapaaksi jos liian pieni

kuhan_pituus = float(input("Hei kalastaja! Kerro minulle senttimetreissä kuinka iso kuha on: "))
print(f"Kuhasi on {kuhan_pituus} cm pitkä")

# kysyy kuhan pituutta
if kuhan_pituus >= 42:
    print("Laita kuha koriin. Kuha on yli 42cm pitkä! Sinun ei tarvitse päästää sitä vapaaksi!")

# jos kuhan pituus on alle 42cm, ohjelma kehottaa päästää sen vapaaksi.
if kuhan_pituus < 42:
    print("Päästä kuha vapaaksi. Se on liian pieni. Kuhan täytyy olla yli 42cm, jotta voit pitää sen!!!")
    print(f"Kuhasi täytyy olla {42 - kuhan_pituus:.2f} cm pidempi")
# kuhan lakisääteinen alamitta on 42 senttimetriä

#jos kuhan pituus on yli 42 ohjelma kehottaa lähtemään risteilylle ja kysyy minkä hytin haluat.
if kuhan_pituus >= 42:
    print("Voisit sitten vaikka lähteä risteilylle juhlistamaan!")

#jos kuha on liian pieni, ohjelma kysyy haluatko lähteä rentoutumaan risteilylle
if kuhan_pituus < 42:
    print("Haluatko lähteä vaikka risteilylle rentoutumaan? ... ensi kerralla se iso kuha nappaa!")
    ehto = input("HALUATKO RISTEILYLLE (kyllä/en): ")


# pitää saada arvo haluatko risteilylle vastaukselle, onko se kyllä vai ei
# kun kirjoittaa ei

# Tehtävä 2, kysyy laivan hyttiluokan (LUX, A, B, C), sen jälkeen tulostaa sen sanallisen kuvauksen.
#  tehtävässä on käytettävä if/elif/else-toistorakennetta!!

#eli kysy ensin laivan hyttiluokka

laivan_hytti = float(input("Kirjoita tähän haluamasi laivan hytti: "))
