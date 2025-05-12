class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4 / 3) * 3.142 * (self.radius ** 3)

s1 = Sphere(int(input("Enter radius : ")))
print(s1.volume())

