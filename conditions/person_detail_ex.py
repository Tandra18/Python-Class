name = input("Enter name : ")
age = int(input("Enter age : "))
gender = input("Enter gender M (or) F : ")
height = float(input("Enter height : "))

match gender:
    case "M":
        print(f"His name is Mr.{name}.")
        if 0 < age < 20:
            print(f"He is {age} years old.And a teenager!")
        elif 21 < age < 30:
            print(f"He is {age} years old.And an adult!")
        elif 31 < age < 45:
            print(f"He is {age} years old.And a middle aged!")
        elif 46 < age < 60:
            print(f"He is {age} years old.And an old man!")
        elif age >= 60:
            print(f"He is {age} years old.And a grandpa!")
        print(f"His height is {height} m .")

    case "F":
        print(f"Her name is Mrs.{name}.")
        if 0 < age < 20:
            print(f"She is {age} years old.And a teenager!")
        elif 21 < age < 30:
            print(f"She is {age} years old.And an adult!")
        elif 31 < age < 45:
            print(f"She is {age} years old.And a middle aged!")
        elif 46 < age < 60:
            print(f"She is {age} years old.And an old woman!")
        elif age >= 60:
            print(f"She is {age} years old.And a grandma!")
        print(f"Her height is {height} m .")

    case _:
        print("Pls enter a valid gender, M or F .")