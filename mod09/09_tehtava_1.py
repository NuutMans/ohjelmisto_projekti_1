class Car:
    def __init__(self, register_number, top_speed):
        print("New car has been created")
        self.register_number = register_number
        self.top_speed = top_speed
        self.speed = 0
        self.trip = 0

    def accelerate(self, speed_change):
        # Muutetaan nopeutta
        self.speed += speed_change

        # Huippunopeus
        if self.speed > self.top_speed:
            self.speed = self.top_speed

        # Nopeus ei saa olla negatiivinen
        if self.speed < 0:
            self.speed = 0


# Ohjelma
car1 = Car("ABC-123", 142)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(-50)

print(
    f"Auton 1 tiedot:\n"
    f"Rekkari: {car1.register_number}\n"
    f"Huippunopeus: {car1.top_speed} km/h\n"
    f"Nopeus: {car1.speed} km/h\n"
    f"Matka: {car1.trip} km"
)