class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height
        print("Created!")
        
    def area(self):
        return 0.5 * self.base * self.height


tr1 = Triangle(10, 5)

print(tr1.area())

