class Shape:
    def __init__(self, name="Shape"):
        self.name = name

    def area(self):
        return 0

    def display_area(self):
        print(f"Area of {self.name} is {self.area()}")

    def __str__(self):
        return f"This is a {self.name}"

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.142 * (self.radius ** 2)

# Test input and output
rectangle = Rectangle(float(input("Enter width of rectangle: ")), float(input("Enter height of rectangle: ")))
rectangle.display_area()
print(rectangle)

triangle = Triangle(float(input("\nEnter base of triangle: ")), float(input("Enter height of triangle: ")))
triangle.display_area()
print(triangle)

circle = Circle(float(input("\nEnter radius of circle: ")))
circle.display_area()
print(circle)
