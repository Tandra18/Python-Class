# def my_function(name, age):
#     print("Name:", name)
#     print("Age:", age)
#
# my_function(age=25, name="Alice")

def introduce(name, city):
    print(f"My name is {name} and I live in {city}.")

introduce(name="John", city="New York")
introduce(city="Yangon", name="Aye Aye")


def greet(name="Guest"):
    print(f"Hello, {name}!")

greet() # default value
greet(name="Su Su")

