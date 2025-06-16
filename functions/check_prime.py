def is_prime(n):
    if n < 2:
        return "It is not a prime number!"

    for i in range(2, int(n ** 0.5) + 1): #[1:4]
        if n % i == 0:
            return "It is not a prime number!"
    return "It is a prime number!"

result = is_prime(int(input("Enter a number : ")))
print(result)


