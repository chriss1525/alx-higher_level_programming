#!/usr/bin/python3
""" this module reads a text file and prints it to stdout"""


def read_file(filename=""):
    """
    reads a file
    prints it to stdout
    """
    with open(filename,  encoding="utf-8") as file:
        read = file.read()
        print(read, end="")
