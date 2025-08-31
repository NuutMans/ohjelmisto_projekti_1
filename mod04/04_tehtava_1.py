# mod04 tehtävä 1

i = 1  # ensimmäinen numero josta alkaa tarkistamaan
toistojenlkm = 1000 # toistojen lukumäärä

while i <= toistojenlkm:  # toistojen lukumäärää voi muokata muuttujan kohdala
    if i % 3 == 0:  # jos jaollinen 3:lla - niin tulosta luku
        print(i) # tulosta kolmella jaollinen luku
    i += 1 # integerin arvo + 1. Tän jälkeen looppi alkaa alusta, kunnes käynyt läpi toistojenlkm-muuttujan lukumäärän