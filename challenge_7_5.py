numbers1 = [8, 19, 148, 4]
numbers2 = [9, 1, 33, 83]

multi = []

for i in range(4):
    for j in range(4):
        multi.append(numbers1[i] * numbers2[j])

print (multi)


"""or

for i in numbers1:
    for j in numbers2:
        multi.append(i * j)

print(multi)
"""