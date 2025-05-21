def fruit():
    price = 600 #Enclosing scope
    print("This is a fruit!")
    def apple():
        print(f"Apple price is {price}")
    apple()
fruit()

