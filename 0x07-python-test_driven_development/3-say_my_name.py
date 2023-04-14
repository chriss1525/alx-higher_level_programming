#!/usr/bin/python3
"""this module holds the function say_my_name"""


def say_my_name(first_name, last_name=""):
    """print name: my name is {first_name} {second_name}"""
    if not isinstance(first_name, str):
        """check if first name is a string"""
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        """check if last name is a string"""
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
