class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4 / 3) * 3.142 * (self.radius ** 3)

r = int(input("Enter radius : "))
s1 = Sphere(r)
print(f"The volume of a sphere is {s1.volume()}")

