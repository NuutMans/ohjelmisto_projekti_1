import random

def number(sides):
    return random.randint(1, sides)

sides = int(input("Anna nopan sivujen määrä: "))

app_running = True
while app_running:
    result = number(sides)
    print (result)
    if result == sides:
        app_running = False



