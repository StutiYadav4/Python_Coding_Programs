class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):

    def move(self):
        print("drive")


class Boat(Vehicle):

    def move(self):
        print("sail")


class Plane(Vehicle):

    def move(self):
        print("fly")


car1 = Vehicle("ford", "mustang")
boat1 = Boat("hi", "there")
plane1 = Plane("boeing", "747")

for i in (car1, boat1, plane1):
    i.move()



