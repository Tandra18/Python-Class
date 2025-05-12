# #Multiplication Table
# num = int(input("Enter a number : "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")
#
# #Sum of numbers from 1 to 100
# total = 0
# for i in range(1,101):
#     total += i
# print("Sum : ", total)

# #Print number from 10 to 1
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

# #Sum of digits of a number
# num = 1234
# sum_digit = 0
# while num > 0:
#     sum_digit += num % 10
#     num //= 10
# print("Sum of digits is ", sum_digit)

#Guess number
secret = 7
guess = int(input("Enter a guess number :"))
while guess != secret:
    guess = int(input("Wrong! Try again! : "))
print("Correct!")