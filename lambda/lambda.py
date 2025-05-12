# add = lambda x, y: x + y
# print(add(5, 3))
#
# calculate = lambda a, b, c: a + b * c
# print(calculate(5, 3, 2))
#

# def my_func(n):
#     return lambda x: x * n
#
# doubler = my_func(2)
# print(doubler(11))
#

# students = [
#     ('Aung Aung', 85),
#     ('Mya Mya', 92),
#     ('Ko Ko', 78)
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
#

# words = ["hi", "hello", "me", "python", "java", "AI"]
# long_words = list(filter(lambda x: len(x) > 3, words))
# print(long_words)

celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)  # Output: [32.0, 50.0, 68.0, 86.0]


