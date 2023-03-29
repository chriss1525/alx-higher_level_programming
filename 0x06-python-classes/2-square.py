#!/usr/bin/python3
"""class square"""


class Square:
    """define object size"""

    def __init__(self, size=0):
        """initialize size"""
        if type(size) is int:
            if size >= 0:
                self.__size = size
                """handle errors"""
            else:
                raise ValueError("size must be >=0")
        else:
            raise TypeError("size must be an integer")
