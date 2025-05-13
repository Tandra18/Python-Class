class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return (1/2) * self.base * self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.142 * (self.radius ** 2)

rectangle = Rectangle(float(input("Enter width of rectangle : ")), float(input("Enter height of rectangle : ")))
print(f"Area of rectangle is {rectangle.area()}\n")

triangle = Triangle(float(input("Enter base of triangle : ")), float(input("Enter height of triangle : ")))
print(f"Area of triangle is {triangle.area()}\n")

circle = Circle(float(input("Enter radius of circle :")))
print(f"Area of circle is {circle.area()}\n")