'''Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.'''

import random


def number():
    number_cube = random.randint(1,6)
    return number_cube

app_running = True

while app_running:
    numbers = number()
    print (numbers)
    if numbers == 6:
        app_running = False