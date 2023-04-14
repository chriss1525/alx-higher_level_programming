#!/usr/bin/python3
"""this module defines print_square"""


def print_square(size):
    """prints a square of side size using the # symbol"""
    if not isinstance(size, int):
        """check if size is an integer"""
        raise TypeError("size must be an integer")
    if size < 0:
        """check if size is greater than 0"""
        raise ValueError("size must be >= 0")
    print((("#" * size) + "\n") * size, end="")
