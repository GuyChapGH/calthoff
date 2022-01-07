class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

class Square():
    def __init__(self, s1):
        self.s1 = s1
    
    def calculate_perimeter(self):
        return self.s1 * 4

rec1 = Rectangle(10, 20)

sq1 = Square(10)

print(rec1.calculate_perimeter())

print(sq1.calculate_perimeter())

