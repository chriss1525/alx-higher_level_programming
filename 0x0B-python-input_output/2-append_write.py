#!/usr/bin/python3
"""append string to the end of a file"""


def append_write(filename="", text=""):
    """
    args: filename and text to be added to the file
    add text to the end of filename

    """
    with open(filename, 'a') as file:
        file.write(text)
        print(len(text))
