#Parent class
class Animals:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

#Child class
class Dog(Animals):
    def __init__(self,name,breed,age):
        # Calling parent class __init__()
        super().__init__(name)
        self.breed = breed
        self.age = age

    def speak(self):
        print(f"{self.name} is the {self.breed}.Age is {self.age}.")

    def adopt(self):
        print(f"Bring {self.name} to adopt!")

my_dog = Dog("Lucky","Golden Retriever",2)
my_dog.speak()
my_dog.adopt()

