class Animal:
    def speak(self):
        print("animal makes sound")

class Dog(Animal):
    def bark(self):
        print("dog bark")

class lion(Animal):
    def Roar(self):
        print("Lion Roar")

d =Dog()
l =lion()
d.speak()
d.bark()
l.Roar()
l.speak()