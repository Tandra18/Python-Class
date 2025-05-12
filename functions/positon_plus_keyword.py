def details(name, age, /, *, gender, address):
    print(f"{name} is {age} years old.")
    print(f"Gender is {gender}.")
    print(f"Lives in {address}")

details("Aung Aung", 34, gender="Male", address="yangon")


