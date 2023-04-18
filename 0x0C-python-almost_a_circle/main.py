#!/usr/bin/python3
""" Check """
from models.square import Square

s = Square(2)
if str(s) != "[Square] (1) 0/0 - 2":
    print("__str__ is not correctly overloaded: {}".format(s))
    exit(1)

s = Square(2, 3)
if str(s) != "[Square] (2) 3/0 - 2":
    print("__str__ is not correctly overloaded: {}".format(s))
    exit(1)

s = Square(2, 3, 4)
if str(s) != "[Square] (3) 3/4 - 2":
    print("__str__ is not correctly overloaded: {}".format(s))
    exit(1)

s = Square(2, 3, 4, 89)
if str(s) != "[Square] (89) 3/4 - 2":
    print("__str__ is not correctly overloaded: {}".format(s))
    exit(1)

print("OK", end="")
