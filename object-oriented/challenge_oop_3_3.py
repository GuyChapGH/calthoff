class Person():
    def __init__(self, name):
        self.name = name

def test(obj1, obj2):
    return obj1 is obj2

p1 = Person("Guy")

p2 = Person("Steve")

p3 = p1

print(test(p1, p2))

print(test(p1, p3))