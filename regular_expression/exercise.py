import re

# txt = "My phones are 09265266985 and 09785641236"
# phones = re.findall(r"09\d{8}",txt)
# print(phones)


greeting = "My name1 is narijgeojsw32 Zaw Ye Naung2."
cap = re.findall(r'\b[A-Z][a-z]*',greeting)
name = re.findall(r'\bna\w*',greeting,flags=2)
print(cap) #narijgeojsw32
print(name)