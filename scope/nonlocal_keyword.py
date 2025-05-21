def food():
    name = "apple"
    def fruit():
        nonlocal name
        name = "banana"
    fruit()
    return name
print(food())


# def person():
#     name = "Yin Mon"
#     age = None
#     print(f"Name is {name}")
#
#     def details():
#         nonlocal age
#         age = 38
#         print(f"Age is {age}")
#
#     details()
#
#     def info():
#         phone = "0912345678"
#         print(f"Contact is {phone}.")
#         print(f"Age is {age}")
#
#     info()
#
#
# person()
