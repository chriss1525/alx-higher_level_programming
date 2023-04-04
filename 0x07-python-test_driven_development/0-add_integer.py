#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    elif type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
