#!/usr/bin/python3
"""
writes string to a text file
returns number of characters writen
"""


def write_file(filename="", text=""):
    """ write text in file and return number of characters written"""
    with open(filename,  'w') as file:
        instruct = file.write(text)
        return instruct
