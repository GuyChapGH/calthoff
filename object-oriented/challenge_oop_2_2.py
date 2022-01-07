class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4
# change_size increases size by inc_size amount
    def change_size(self, inc_size):
        self.s1 += inc_size

sq1 = Square(100)
print(sq1.s1)

sq1.change_size(100)
print(sq1.s1)

