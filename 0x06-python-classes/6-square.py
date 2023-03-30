#!/usr/bin/python3
"""
class square has private instance size and public instance are
if size is not an integer raise type error
if size is less than 0 raise value error
"""


class Square:
    """
    takes in private instance size, private instance positions and public instance area
    """

    def __init__(self, size=0, position=(0, 0)):
        """define object size
        define object postition"""
        self.__size = size
        self.position = position

    @property
    def size(self):
        """get access to private instance size
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

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """check if position is a tuple of two positive integers"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """public instace attribute area.
        returns the value of the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """print to stdout the square to the character #"""
        if self.__size == 0:
            print()
            return
        for y in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
