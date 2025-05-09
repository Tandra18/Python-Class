# my_tuple = (10, 20, 30)
# print(f"Tuple : {my_tuple}")
#
# temp_list = list(my_tuple)  # Convert to list
# print(f"Temp list {temp_list}")
# temp_list[1] = 99  # Update value
# print(f"Updated temp list {temp_list}")
#
# my_tuple = tuple(temp_list)  # Convert back to tuple
# print(f"Updated tuple : {my_tuple}")  # Output: (10, 99, 30)

# my_tuple = ("apple", "banana", "cherry")
# print(f"My tuple : {my_tuple}")
#
# temp_list = list(my_tuple)
# print(f"Temp list : {temp_list}")
# temp_list.append("orange")
# print(f"Updated temp list : {temp_list}")
#
# my_tuple = tuple(temp_list)
# print(f"Updated my tuple : {my_tuple}")


# my_tuple = (1, 2, 3)
# # Concatenate a new tuple with one element
# my_tuple = my_tuple + (4,)
# print(my_tuple)  # Output: (1, 2, 3, 4)

old_tuple = ("a", "b", "c", "d", "e", "f")
new_tuple = old_tuple[0:5] + ("x",)
print(new_tuple)

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
