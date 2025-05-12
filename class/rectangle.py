class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

r1 = Rectangle(int(input("Enter width : ")), int(input("Enter height : ")))
print(f"Area is {r1.area()}.")
print(f"Perimeter is {r1.perimeter()}.")

