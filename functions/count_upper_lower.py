def count_case(s):
    upper = 0
    lower = 0
    vowels = 0
    for char in s:
        if char.lower() in 'aeiou':
            vowels += 1
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return {"uppercase": upper, "lowercase": lower,"vowels": vowels}
print(count_case(input("Enter a string : ")))

