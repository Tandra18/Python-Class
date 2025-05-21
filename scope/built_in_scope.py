# print("Hello")          # output: Hello
# print(len("Python"))    # output: 6
# print(sum([1, 2, 3]))   # output: 6
# print(type(123))        # output: <class 'int'>
# print(max([1, 2, 3]))   # output: 3
# print(str(123))         # output: '123' → convert to string
# print(int("456"))       # output: 456  → convert to integer
# print(float("3.14"))    # output: 3.14 → convert to float
# print(bool(0))          # output: False → 0 is False
# print(bool(5))          # output: True → non-zero is True
#
# fruits = ['apple','banana','orange']
# print(list(enumerate(fruits,start=0)))


menu = ['Pizza', 'Burger', 'Salad']

print("Menu Options:")
for number, item in enumerate(menu, start=1):
    print(f"{number}. {item}")



# students = ['Aye Aye', 'Zaw Zaw', 'Moe Moe']
#
# for roll,name in enumerate(students,start=1):
#     print(f"Roll number {roll} is {name}.")

