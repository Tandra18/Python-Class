# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def move(self):
#         print("drive")
#
#
# class Boat:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def move(self):
#         print("sail")
#
#
# class Plane:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def move(self):
#         print("fly")
#
#
# car = Car("Honda", "Civic")
# boat = Boat("Yamaha", "SZ 270d")
# plane = Plane("Boeing", "BFL 39i")
#
# for x in (car, boat, plane):
#     x.move()

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def move(self):
#         return "move!"
#
# class Car(Vehicle):
#     pass
#
# class Boat(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand, model)
#         self.brand = brand
#         self.model = model
#
#     def move(self):
#         return "sail!"
#
#
# class Plane(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand, model)
#         self.brand = brand
#         self.model = model
#
#     def move(self):
#         return "fly!"
#
#
# car = Car("Honda", "Civic")
# boat = Boat("Yamaha", "SZ 270d")
# plane = Plane("Boeing", "BFL 39i")
#
# for x in (car, boat, plane):
#     print(f"{x.brand} {x.model} can {x.move()}")
#

class Person:
    def __init__(self,name=None):
        self.name = name

    def greet(self):
        if self.name:
            print(f"Hello {self.name}!")
        else:
            print("Hello")

txt = Person("Zaw")
txt.greet()
