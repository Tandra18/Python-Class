def fibonacci(n):
    if n <= 1:
        return n
        # base case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        # recursive case

for i in range(10):
    print(fibonacci(i), end=" ")

