import re

# txt = "I love dogs.Dogs are adorable."
# result = re.sub('dogs','cats',txt,flags=re.IGNORECASE)
# print(result)

txt = "I love dogs.Dogs are adorable."

def replace_case(match):
    word = match.group()
    if word[0].isupper():
        return "Cats"
    else:
        return "cats"

result = re.sub('dogs', replace_case, txt, flags=2)
print(result)
