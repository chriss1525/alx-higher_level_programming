#!/usr/bin/python3
"""
define class square
if size is not an integer raise type error
if size is less than 0 raise value error
"""


class Square:
    """
    define object size
    size is an int that is greater than or equal to 0
    """

    def __init__(self, size=0):
        """initialize size"""
        if type(size) is int:
            pass
        else:
            raise TypeError("size must be an integer")
        if size >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")
