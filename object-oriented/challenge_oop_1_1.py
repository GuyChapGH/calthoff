class Apple():
    def __init__(self, c, w, v, o):
        self.colour = c
        self.weight = w
        self.variety = v
        self.origin = o
        print("Created!")

app1 = Apple("red", 20, "Red Pippin", "UK")

print(app1)