#!/usr/bin/python3
"""append string to the end of a file"""


def append_write(filename="", text=""):
    with open(filename, 'a') as file:
        file.write(text)
        print(len(text))
