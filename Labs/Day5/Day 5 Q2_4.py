# 4. Demonstrate polymorphism using the same method name with different behaviors

class Dog:
    def speak(self):
        print("Dog barks")


class Cat:
    def speak(self):
        print("Cat meows")


animal = [Dog(), Cat()]

for a in animal:
    a.speak()
