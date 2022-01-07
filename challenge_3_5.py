def get_int():
    while True:
        try:
            r = int(input("Please enter an integer: "))
            return r
        except ValueError:
            print("Integer required")

n = get_int()
m = get_int()

try:
    # special division operator gives floor of division rounded down to nearest integer
    quot = n // m
    print("{} divided by {} gives quotient {}".format(n, m, quot))
except ZeroDivisionError:
    print("Error dividing by zero")

