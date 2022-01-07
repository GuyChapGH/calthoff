def convert(x):
    """
    Returns float from string
    :param x: string.
    :return: float from string.
    """
    try:
        return float(x)
    except ValueError:
        print("Invalid input.")

s = input("Please enter a number: ")

t = convert(s)

if t is not None:
    print(t)