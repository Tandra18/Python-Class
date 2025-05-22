import re

txt = "My name is Zaw Ye Naung"
result = re.search('ye',txt,flags=2)

if result:
    print("Found :", result.group())
else:
    print("Not found!")









