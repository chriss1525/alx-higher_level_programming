#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Returns the sum of a and b

    >>>add_integer(3, 5)
    8
    >>>add_integer(1)
    99
    """
    if type(a) == float:
        """cast floats to integers"""
        a = int(a)
    if type(b) == float:
        b = int(b)
    elif type(a) != int:
        """raise typeerror when number is not a float or integer"""
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
