my_tuple = ("apple", "banana", "cherry")

print(my_tuple[0])  # Output: apple
print(my_tuple[1])  # Output: banana
print(my_tuple[2])  # Output: cherry

print(my_tuple[-1])  # Output: cherry
print(my_tuple[-2])  # Output: banana
print(my_tuple[-3])  # Output: apple

print(my_tuple[0:2])   # Output: ('apple', 'banana')
print(my_tuple[1:])    # Output: ('banana', 'cherry')
print(my_tuple[:2])    # Output: ('apple', 'banana')


nested_tuple = ("a", (1, 2, 3), "b")

print(nested_tuple[1])      # Output: (1, 2, 3)
print(nested_tuple[1][0])   # Output: 1
print(nested_tuple[1][2])   # Output: 3
