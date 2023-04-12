#!/usr/bin/python3
""" this module reads a text file and prints it to stdout"""


def read_file(filename=""):
    """
    reads a file
    prints it to stdout
    """
    with open(filename, 'r') as filename:
        read = filename.read()
        print(read)
