def distance(leg1, leg2, leg3, leg_in=2, leg_out=2):
    """
    Calculates total distance by addition
    :param: leg1: int or float
    :param: leg2: int or float
    :param: leg3: int or float
    :opt param: leg_in: int or float
    :opt param: leg_out: int or float
    : return: sum of leg1, leg2, leg3, leg_in and leg_out.
    """
    return leg1 + leg2 + leg3 + leg_in + leg_out

walk = distance(3.5, 1.5, 2.5)
print("The walk distance is {} miles.".format(walk))
