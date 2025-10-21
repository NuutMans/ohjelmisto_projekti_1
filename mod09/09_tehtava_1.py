class Car():
    def __init__(self):
        print ("New car has been created")
        self.register_number = "ABC-123"
        self.top_speed = 100
        #todo anna huippunopeus ja rekkari alustajan parametreina
        self.speed = 0
        self.trip = 0
    def accelerate(self):
        # todo anna nopeuden muutos parametreina ja huomioi huippunopeus
        # todo auton nopeus ei saa mennä negatiiviseksi, if-else -rakenteita joutuu käyttämään
        self.speed += 5

#hyödynnetään listoja, ei ole järkeä käyttää vaikka sataan autoon car1, car2, car3


car1 = Car(ABC-123, 142)
car1.accelerate()
car1.accelerate()
car2 = Car()

print(f"Auton 1 nopeus: {car1.speed}, auto 2: {car2.speed}")
