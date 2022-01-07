def get_int():
    while True:
        try:
            r = int(input("Please enter an integer: "))
            return r
        except ValueError:
            print("Must be an integer")

age = get_int()

if age == 10:
    print("Welcome Whippersnapper")

if age == 20:
    print("Looking good!")

if age == 30:
    print("The Golden Years")

if age == 40:
    print("Getting on a bit")

if age == 50:
    print("Over the hill?")

if age == 60:
    print("Lucky for you")

if age == 70:
    print("Keep going you old bugger!")

if age == 80:
    print("You're a dinosaur!")
