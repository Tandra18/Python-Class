class Rectangle:
    def __init__(self, width, height):
        self.rectangle_width = width
        self.rectangle_height = height

    def area(self):
        return self.rectangle_width * self.rectangle_height

    def perimeter(self):
        return (self.rectangle_width + self.rectangle_height) * 2

# r1 = Rectangle(int(input("Enter width : ")), int(input("Enter height : ")))
r1 = Rectangle(5,3)
print(f"Area is {r1.area()}.")
print(f"Perimeter is {r1.perimeter()}.")

