def palindrome(s):
    if len(s) <= 1:
        return "It is palindrome!"  # base case
    elif s[0] != s[-1]:
        return "It is not a palindrome"
    else:
        return palindrome(s[1:-1])  # recursive case

result = input("Enter a string : ")
print(palindrome(result))

