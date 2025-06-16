def reverse_string(s):
    if len(s) == 0:
        return s
        # base case
    else:
        return reverse_string(s[1:]) + s[0]
        # recursive case

print(reverse_string(input("Enter a string : ")))  # Output: "olleh"


