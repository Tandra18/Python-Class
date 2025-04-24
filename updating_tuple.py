# my_tuple = (10, 20, 30)
# print(my_tuple)
#
# temp_list = list(my_tuple) # Convert to list
# temp_list[1] = 99 # Update value
#
# my_tuple = tuple(temp_list) # Convert back to tuple
# print(my_tuple)  # Output: (10, 99, 30)

# my_tuple = ("apple", "banana", "cherry")
# temp_list = list(my_tuple)
# temp_list.append("orange")
# my_tuple = tuple(temp_list)

# my_tuple = (1, 2, 3)
# # Concatenate a new tuple with one element
# my_tuple = my_tuple + (4,)
# print(my_tuple)  # Output: (1, 2, 3, 4)

# my_tuple = (1, 2, 3, 4)
# temp_list = list(my_tuple)
#
# temp_list.remove(3)  # remove item
# my_tuple = tuple(temp_list)
#
# print(my_tuple)  # Output: (1, 2, 4)

# old_tuple = ("a", "b", "c")
# # Replace first element
# new_tuple = ("x",) + old_tuple[1:]
# print(new_tuple)  # Output: ('x', 'b', 'c')

# my_tuple = ("apple", "banana", "cherry")
# del my_tuple
# print(my_tuple) #this will raise an error