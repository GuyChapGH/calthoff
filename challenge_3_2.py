while True:
    try:
        n = int(input("Please enter an integer: "))
        break
    except ValueError:
        print("Integer required")

if n >= 10:
    print("You entered an integer greater than or equal to ten")
else:
    print("You entered an integer less than ten")