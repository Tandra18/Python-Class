def count_vowels(s):
    return sum(1 for char in s.lower() if char in 'aeiou')

print(count_vowels(input("String: ")))

