while True:
    try:
        n = int(input("Please enter an integer: "))
        break
    except ValueError:
        print("Integer required")

if n <= 10:
    print("First message")
# Don't need n > 10. This would be picked up by the first 'if' statement.
elif n > 10 and n <= 25:
    print("Second message")
else:
    print ("Third message")