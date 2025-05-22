import re

txt = "There is apple.I like Apple."
result = re.findall('apple',txt,flags=2)
print(result)