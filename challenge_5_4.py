profile = {"height": 1.91, "colour": "blue", "author": "Ian Rankin"}

question = input("Enter 'height', 'colour' or 'author' to get profile item: ")

if question in profile:
    print(profile[question])
else:
    print("Item not found.")