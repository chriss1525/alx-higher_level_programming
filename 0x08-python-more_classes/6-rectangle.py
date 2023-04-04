#!/usr/bin/python3
"""
class rectangle has private instance width and private instance height
"""


class Rectangle:
    """
    takes in private instances width and height
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """define object width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get access tp private instance width
        return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Raise Typeerror if width is not integer
        valueerror if width is less than 0"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get access tp private instance height
        return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Raise Typeerror if height is not integer
        valueerror is height is less than 0"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """public instace attribute area.
        returns the value of the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """public instace attribute area.
        returns the value of the area of the square"""
        if self.__width == 0:
            return 0
        if self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """returns representation of rectangle using #"""

        if self.__height == 0 or self.__width == 0:
            return ''

        string = ''
        for i in range(self.__height):
            for j in range(self.__width):
                string += '#'
            string += '\n'
        return string[: -1]

    def __repr__(self):
        """Returns a string representation of the Rectangle
        that can be used to recreate the object"""
        return "Rectangle({}, {})".format(self.__height, self.__width)

    def __del__(self):
        """prints by rectangle when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
