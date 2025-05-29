# def my_function(*fruits):
#     print(fruits)
#     print("My favorite fruit is ", fruits[3])
#
# my_function("apple", "banana", "cherry","orange")


# def my_function(*fruits):
#     for x in fruits:
#         print(x)
#     if len(fruits) > 1:
#         print("My favorite fruit is", fruits[1])
#     else:
#         print("Not enough fruits to choose a favorite.")
#
# # Get input from the user
# user_input = input("Enter fruits separated by commas: ")
# fruit_list = user_input.split(",")
#
# # Strip whitespace and call the function
# fruit_list = [fruit.strip() for fruit in fruit_list]
# my_function(*fruit_list)
