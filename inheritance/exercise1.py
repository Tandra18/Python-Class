# Base class
class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    def display_info(self):
        print(f"\nCar: {self.make} {self.model}")
        print(f"Price: ${self.price}")

    def purchase(self):
        print(f"You have purchased the {self.make} {self.model} for ${self.price}.\nThank you!")

# Subclass for Electric Car
class ElectricCar(Car):
    def __init__(self, make, model, price, battery_range):
        super().__init__(make, model, price)
        self.battery_range = battery_range

    def display_info(self):
        super().display_info()
        print(f"Battery Range: {self.battery_range} km")

# Subclass for Gasoline Car
class GasCar(Car):
    def __init__(self, make, model, price, fuel_efficiency):
        super().__init__(make, model, price)
        self.fuel_efficiency = fuel_efficiency

    def display_info(self):
        super().display_info()
        print(f"Fuel Efficiency: {self.fuel_efficiency} km/l")

# Simulate car selection and purchase
print("Welcome to the Car Shop!\n")

car_type = input("Select car type (electric/gas): ").strip().lower()

if car_type == "electric":
    car = ElectricCar("Tesla", "Model 3", 35000, 450)
elif car_type == "gas":
    car = GasCar("Toyota", "Corolla", 22000, 18)
else:
    print("Invalid car type selected.")
    exit()

car.display_info()

confirm = input("\nDo you want to purchase this car? (yes/no): ").strip().lower()
if confirm == "yes":
    car.purchase()
else:
    print("Purchase cancelled.")
