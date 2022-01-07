"""numbers = ["1", "7", "10", "15"]

while True:
    # Remember input returns a string. So numbers have to be strings not int.
    n = input("Please enter an integer (q to quit): ") 
    if n == "q":
        break
    if n in numbers:
        print("Successful guess")
    else:
        print("Not a successful guess")
"""

# Alternative (with numbers as int):

numbers = [1, 7, 10, 15]

while True:
    
    n = input("Please enter an integer (q to quit): ") 
    if n == "q":
        break
    try:
        n = int(n)
    except ValueError:
        print("Please type a number or q to quit")
    # 'continue' avoids printing "Not a successful guess"
        continue
    
    if n in numbers:
        print("Successful guess")
    else:
        print("Not a successful guess")


