tuple1 = ("a", "b", "c", "a")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
print(tuple3.count(3))

basket = ("apple", "banana", "cherry")
new_basket = basket * 2
print(new_basket)

basket = ("apple", "banana", "apple", "cherry")

print(basket.count("apple"))

first_apple = basket.index("apple")
print(f"The index of first apple is {first_apple}")

second_apple = basket.index("apple", first_apple + 1)
print(f"The index of second apple is {second_apple}")
