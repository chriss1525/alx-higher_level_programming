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

    @property
    def size(self):
        """get access tp [rivate instance size
        return square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Raise Typeerror if size is not integer
        valueerror is size is less than 0"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """public instace attribute area.
        returns the value of the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """print to stdout the square to the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                print("#" * self.__size)
