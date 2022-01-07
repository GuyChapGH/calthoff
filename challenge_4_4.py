def halved(x):
    """
    Returns x/2
    :param x: int
    :return: halves x
    """
    return x/2

def multiply(y):
    """
    Returns y*4
    :param y: int
    :return: y multiplied by 4
    """
    return y*4

# Calculation here. Note int() function takes integer part of float, int(0.5)==0
v = halved(1)
w = multiply(int(v))

print(w)