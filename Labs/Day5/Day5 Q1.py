class vehicle:
    vehicle_count = 0
    def __init__(self):
        vehicle.vehicle_count += 1

    def start(self):
        print("Vehicle start")

class car(vehicle):
    def drive(self):
        print("car is driving")

class Bike(vehicle):
    def move(self):
        print("bike is moving")


v1 = vehicle()
c = car()
b = Bike()
v1.start()
c.start()
c.drive()
b.start()
b.start()

print("total vehicles created:", vehicle.vehicle_count)


