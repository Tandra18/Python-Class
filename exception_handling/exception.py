# try:
#     x = 10 / 0
#     print(x)
# except ZeroDivisionError:
#     print("Cannot be divided by 0")

# num = int(input("Enter a number : "))
# if num > 10:
#     raise Exception("Number cannot be greater than 10!")

# num = 'hello'
# if not type(num) is int:
#     raise TypeError("num must be an integer!")


num1_input = input("Enter first number : ")
num2_input = input("Enter second number : ")

try:
    num1 = int(num1_input)
    num2 = int(num2_input)
    total = num1 + num2
    print(f"Total is {total}.")

except ValueError:
    print("Please enter valid numbers!")

print(num1_input,num2_input)





# num = input("Enter a number : ")
# try:
#     num = int(num)
#     result = 100 / num
#     print(f"100 / {num} = {result}")
# except (ValueError,ZeroDivisionError) as e:
#     print("It is not a number (or) cannot be divided by 0!",e)
