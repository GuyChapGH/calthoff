import re


# '*' the preceding item will be matched zero or more times
# '.' this matches any character
# '__.*__' matches any character between and including the two double underscores
# in this form it is greedy and matches as much text as possible.
# '__.*?__' with the question mark it is non-greedy and looks for least number of matches possible

t = "__one__ __two__ __three__"

found = re.findall("__.*?__", t)

for match in found:
    print(match)
