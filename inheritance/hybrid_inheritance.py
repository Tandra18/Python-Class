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

