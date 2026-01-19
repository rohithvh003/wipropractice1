class animal:
    def sound(self):
        print("animal sound")

class dog(animal):
    def sound(self):
        print("Dog Barks")

class cat(animal):
    def sound(self):
        print("cat Meows")

obj = [dog(),cat()]

for a in obj:
    a.sound()
