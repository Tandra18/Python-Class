price = 400
print(f"Global price is {price}")
def fruit():
    global price
    price = 600
    print(f"Local price {price}")
fruit()
print(f"Now global price is {price}")
