import re

# matches t followed by o or w followed by o

string = "Two too."

m = re.findall("t[wo]o", string, re.IGNORECASE)

print(m)