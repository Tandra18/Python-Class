# add = lambda x, y: x + y
# print("The result is ", add(int(input("Enter x : ")),int(input("Enter y : "))))
#
#
# calculate = lambda a, b, c: a + b * c
# input_a = int(input("Enter a : "))
# input_b = int(input("Enter b : "))
# input_c = int(input("Enter c : "))
# result = calculate(input_a,input_b,input_c)
# print("Result is ",result)





# def my_func(n):
#     return lambda x: x * n
#
# doubler = my_func(2)
# print(doubler(11))

# def my_func(n):
#     multi = lambda x: x * n
#     print("The result is ",multi(3))
#
# my_func(2)

# students = [
#     ('Aung Aung', 85 , "C"), #0
#     ('Mya Mya', 92 , "A"), #1
#     ('Ko Ko', 78 , "B") #2
# ]
#
# # Sort by score using lambda
# students.sort(key=lambda x: x[1])
# print(students)

# students = [
#     {"name": "Aung Aung", "age": 24},
#     {"name": "Ma Ma", "age":32},
#     {"name": "Mya Mya", "age":29}
#
# ]
# students.sort(key=lambda x: x["age"],reverse=True)
# print(students)


# words = ["hi", "hello", "me", "python", "java", "AI"]
# long_words = list(filter(lambda x: len(x) > 3, words))
# print(long_words)



celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)  # Output: [32.0, 50.0, 68.0, 86.0]


a = 1
b = 2
add = a + b
print(add)