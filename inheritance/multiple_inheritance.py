# class Parent1:
#     pass
# class Parent2:
#     pass
#
# # Multiple Inheritance
# class Child(Parent1, Parent2):
#     pass

# class Father:
#     def skills(self):
#         print("Gardening, Carpentry")
#
# class Mother:
#     def skills(self):
#         print("Cooking, Art")
#
# class Child(Father, Mother):
#     def my_skills(self):
#         print("I have my parents skills:")
#         Father.skills(self)
#         Mother.skills(self)
# c = Child()
# c.my_skills()

# #Method overriding
# class A:
#     def show(self):
#         print("This is A!")
#
# class B:
#     def show(self):
#         print("This is B!")
#
# class C(B,A):
#     pass
#
# result = C()
# result.show()


class X:
    def action(self):
        print("X action")

class Y(X):
    def action(self):
        print("Y action")
        super().action()

class Z(X):
    def action(self):
        print("Z action")
        super().action()

class A(Y, Z):
    def action(self):
        print("A action")
        super().action()

a = A()
a.action()
print(A.mro())

