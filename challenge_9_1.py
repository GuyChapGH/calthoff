import os

fp = os.path.join("C:\\", "Users", "Admin", "Python", "test.txt")

print(fp)

# with open(fp, "r") as f:
#    print(f.read())


content = []

with open(fp, "r") as f:
    content.append(f.read())

print(content)

