# #Multiplication Table
# num = float(input("Enter a number : "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")


# #Sum of numbers from 1 to 100
# result = 0
# for i in range(1, 16):
#     result += i
# print("Sum is ",result)


# #Print number from 10 to 1
# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

#Sum of digits of a number
num = int(input("Enter Number : "))
sum_digit = 0
while num > 0:
    sum_digit += num % 10
    num //= 10
print("Sum of digits is ", sum_digit)

# # Guess number
# secret = 7
# guess = int(input("Enter a guess number :"))
# while guess != secret:
#     guess = int(input("Wrong! Try again! : "))
#
# print("Correct!")



