def get_int():
    while True:
        try:
            r = int(input("Please enter an integer: "))
            return r
        except ValueError:
            print("Must be an integer")

n = get_int()
m = get_int()

try: 
    rem = n % m
    print("Remainder of {} divided by {} is {}".format(n, m, rem))
except ZeroDivisionError:
    print("Division by zero error")

