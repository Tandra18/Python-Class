import re

name = input("Enter name : ").strip().title()


while True:
    age_input = input("Enter age : ")
    try:
        age = int(age_input)
        if age > 0:
            break
        else:
            print("Age must be greater than 1!")
    except ValueError:
        print("Age must be integer!")


while True:
    gender = input("Enter gender : ")
    if gender in ('male','m','Male','M','female','f','Female','F'):
        break
    else:
        print("Please enter a valid gender.")

while True:
    height_input = input("Enter height in meter : ")
    try:
        matches = re.findall(r'\d+(?:\.\d+)?',height_input)
        if not matches:
            print("Include values of height!")
        height = float(matches[0])
        if float(height) < 1:
            print("Height must be greater than 0 m!")
        else:
            break
    except (ValueError,IndexError):
        print("Height must be integer or float!")


match gender:
    case 'male'|'m'|'Male'|'M':
        if 0 < age < 13:
            print(f"His name is {name}.\n"
                  f"He is a {age} years old boy.\n"
                  f"His height is {height} m.")
        elif 12 < age < 20:
            print(f"His name is {name}.\n"
                  f"He is a {age} years old teenager.\n"
                  f"His height is {height} m.")
        elif 20 < age < 36:
            print(f"His name is {name}.\n"
                  f"He is a {age} years old adult.\n"
                  f"His height is {height} m.")
        elif 35 < age < 46:
            print(f"His name is {name}.\n"
                  f"He is a {age} years old middle age man.\n"
                  f"His height is {height} m.")
        elif 45 < age < 61:
            print(f"His name is {name}.\n"
                  f"He is a {age} years old old man.\n"
                  f"His height is {height} m.")
        else:
            print(f"His name is {name}.\n"
                  f"He is a {age} years old grandpa.\n"
                  f"His height is {height} m.")

    case 'female' | 'f' | 'Female' | 'F':
        if 0 < age < 13:
            print(f"Her name is {name}.\n"
                  f"Her is a {age} years old girl.\n"
                  f"Her height is {height} m.")
        elif 12 < age < 20:
            print(f"Her name is {name}.\n"
                  f"He is a {age} years old teenager.\n"
                  f"Her height is {height} m.")
        elif 20 < age < 36:
            print(f"Her name is {name}.\n"
                  f"She is a {age} years old adult.\n"
                  f"Her height is {height} m.")
        elif 35 < age < 46:
            print(f"Her name is {name}.\n"
                  f"She is a {age} years old middle age woman.\n"
                  f"Her height is {height} m.")
        elif 45 < age < 61:
            print(f"Her name is {name}.\n"
                  f"She is a {age} years old old woman.\n"
                  f"Her height is {height} m.")
        else:
            print(f"Her name is {name}.\n"
                  f"She is a {age} years old grandmom.\n"
                  f"Her height is {height} m.")


