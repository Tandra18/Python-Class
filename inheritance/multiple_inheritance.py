# class Parent1:
#     pass
# class Parent2:
#     pass
#
# # Multiple Inheritance
# class Child(Parent1, Parent2):
#     pass

class Father:
    def skills(self):
        print("Gardening, Carpentry")

class Mother:
    def skills(self):
        print("Cooking, Art")

class Child(Father, Mother):
    def my_skills(self):
        print("I have my parents skills:")
        Father.skills(self)
        Mother.skills(self)
c = Child()
c.my_skills()
