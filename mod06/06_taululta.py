# funktio-esimerkkejä
import random


# funktio, joka ei ota parametrejä eikä palauta mitään
def say_hello():
    print("moi")
    print("sinä")

# funktio, joka ottaa vastaan parametrin
def say_hello_v2(username, age): # tekee tyhjän muuttujan joka on käytössä (vain?)muuttujan sisällä
    #print("moi")
    #print(username)
    #print(f"ikäsi: {age}")
    username = username.capitalize() # muuttaa ensimmäisen kirjaimen isoksi
    return f"Hello {username}!, age: {age}" # funktio joka palauttaa (print)
    # ei tarvitse mitään muuta määrettä. voi olla vain return


# funktio joka palauttaa (print)
# funktio palauttaa (return)

# print (say_hello()) # suorittaa funktion ja tulostaa paluuarvon None
# say_hello()
print(say_hello_v2("nuutti", 2))
nimi = "maija"
return_value = say_hello_v2(nimi, 5)
print(return_value)
print(f"nimi muuttuu")


## summa-funktio

numbers = [1, 2, 3, 4, 5]
print (sum(numbers)) # valmis sisäänrakennettu (built-in) funktio (sum)
print(sum([8, 9, 10]))

## oma funktion toteutus, tehdään funktio siis itse (summa + 100)
def my_sum(number_list):# number_list toimii vain muuttujan sisällä (lokaali muuttuja)
    total = 0 # käy kaikki alkiot läpi, oli niitä kuinka monta tahansa
    number_list.append(100) # lisää listaan/summaan aina 100 ylimääräisenä alkiona (alkiona eli osana listaa)
    for num in number_list:
        total = total + num
    return(total) # printissä ei ole järkeä, tehdään paluuarvo (return)

# samat tulostukset kummastakin
print(my_sum(numbers))
print(f"alkuperäisen numbers-muuttujan arvo pääohjelmassa: {numbers}")
print(my_sum(([8, 9, 10])))


# listat ja muuttujat
## katso ja kirjoitakommentit taululla tehdyn esimerkin

list = [1, 2]
list2 = list # list2 viittaa samaan listaan muistissa
list2.append(3) # koska kyseessä sama lista, myös list1 sisältö muuttuu
print(f"muuttujat list: {list} ja list2: {list2} viittaavat samaan listaan muistissa")
# listasta voidana luoda myös uusi kopio: list.copy()


## funktiot ja ohjelman rakenne (alkuperäiset koodit mod4 esimerkistä)

def sum_calculator(num1, num2):
    return num1 + num2


def circumfence(num1, num2):
    return num1 + num2 + num1 + num2


def calculator():
    luku1 = float(input("anna ensimmäinen luku: "))  # esim. "10" -> 10.0
    luku2 = float(input("anna toka luku: "))  # esim. "20" -> 20.0
    total = sum_calculator(luku1, luku2)
    print(f"Yhteenlaskutoimituksen tulos: {total}")
    print(f"Suorakilmion piiri, jossa leveys {luku1} ja korkeus "
          f"{luku2} on: {circumfence(luku1, luku2)}")

def coin_simulator():
    n = 10000
    i = 0
    kolikko_pystyssa_lkm = 0
    while i < n:
        i += 1
        satunnaisluku = random.randint(0, 1000)
        print(f"Arvottu luku: {satunnaisluku}")
        if satunnaisluku < 500:
            print("Kruuna")
        elif satunnaisluku > 500:
            print("Klaava")
        else: # toteutuu muissa tapauksissa, eli jo arvottu luku on tasan 50 (tod.näk: 1/100
            print("Kolikko jäi pystyyn!!!")
            kolikko_pystyssa_lkm += 1
    print(f"Kolikko jäpi pystyyn {kolikko_pystyssa_lkm} kertaa.")



# komentorivisovellus / komentokehotesovellus, modattu / modifioitu
app_running = True # muuttujan nimi kertoo miten sovellus toimii, helpottaa lukemista kun kuvaa dataa mikä siellä on sisällä
# "main loop"
while app_running:
    command = input("Komento> ")
    print(f"Komentosi oli: {command}")
    if command == "lopeta":
        app_running = False
    elif command == "laskukone":
        calculator() # kutsutaan laskukonetta päälooppiin (main loop) menee yllä olevaan funktioon calculator()
    elif command == "kolikkopeli":
        coin_simulator() # kutsutaan kolikkopeliä



