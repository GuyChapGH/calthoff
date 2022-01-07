import math

class Circle():
    def __init__(self, r):
        self.radius = r
        print("Created!")

    def area(self):
        return math.pi * self.radius ** 2

circ1 = Circle(10)

print(circ1.area())