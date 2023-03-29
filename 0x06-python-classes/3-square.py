#!/usr/bin/python3
"""
class square has private instance size and public instance are
if size is not an integer raise type error
if size is less than 0 raise value error
"""


class Square:
    """
    takes in private instance size and public instance area
    """

    def __init__(self, size=0):
        """define object size
    size is an int that is greater than or equal to 0"""
        if type(size) is int:
            pass
        else:
            raise TypeError("size must be an integer")
        if size >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        """public instace attribute area.
        returns the value of the area of the square"""
        return (self.__size ** 2)
