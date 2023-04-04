#!/usr/bin/python3
"""locked class that stops user from dynamically creating new instance"""


class LockedClass:
    """
    empty class
    """
    """define allowed instance"""
    __slots__ = ('first_name')
    pass
