def palindrome(s):
    if len(s) <= 1:
        return True  # base case
    elif s[0] != s[-1]:
        return False
    else:
        return palindrome(s[1:-1])  # recursive case

print(palindrome("madam"))   # Output: True
print(palindrome("hello"))   # Output: False

