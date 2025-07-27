def fruit():
    price = 600 #Enclosing scope
    print(f"Fruit price is {price}")
    def apple():
        nonlocal price
        price = 1000
        color = 'red'
        print(f"Apple price is {price}")
        print(f"Color is {color}")
    apple()
    print(f"Now, fruit price is {price}")
fruit()



# def food():
#     name = 'apple'
#     print(name)
#     def fruit():
#         nonlocal name
#         name = 'banana'
#     fruit()
#     print(name)
# food()

