# class Person:
#     def __init__(self,name,age):
#         print("Creating details..")
#         self.person_name = name
#         self.person_age = age
# p1 = Person("Sandar",32)
# print(p1.person_name)
# print(p1.person_age)


class Person:
    def __init__(self,name,age):
        self.person_name = name
        self.person_age = age

    def __str__(self):
        return f"Name is {self.person_name}.Age is {self.person_age}"
p1 = Person("Sandar",32)
p2 = Person("Zaw Ye",34)
print(p1)
print(p2)