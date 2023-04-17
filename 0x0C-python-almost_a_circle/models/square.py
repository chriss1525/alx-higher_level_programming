#!/usr/bin/python3
"""this module defines a class square
that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """takes in similar arguments to rectangle"/
        "replaces width and height with size"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value


def update(self, *args,  **kwargs):
    """assign argument to every attribute"""
    if args and len(args) != 0:
        try:
            if args[0] is None:
                self.__init__(self.size, self.x, self.y)
            else:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
        except Exception:
            pass
    elif kwargs and len(kwargs) != 0:
        for i, j in kwargs.items():
            if i == "id":
                if j is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    self.id = j
            elif i == "width":
                self.width = j
            elif i == "height":
                self.height = j
            elif i == "x":
                self.x = j
            elif i == "y":
                self.y = j


def to_dictionary(self):
    """Return the dictionary representation of a Rectangle."""
    return {
        "id": self.id,
        "size": self.size,
        "x": self.x,
        "y": self.y
    }