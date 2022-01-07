answer = input("What is your name?: ")

with open("test1.txt", "w") as f:
    f.write(answer)

