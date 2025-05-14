class Animal:
    def breathe(self):
        print("I can breathe.")

class Mammal(Animal):
    def feed_milk(self):
        print("I can feed milk.")

class Human(Mammal):
    def speak(self):
        print("I can speak.")


h = Human()
h.breathe()     # from Animal
h.feed_milk()   # from Mammal
h.speak()       # from Human

