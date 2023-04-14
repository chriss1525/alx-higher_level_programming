#!/usr/bin/python3
"""this module defines text_indentation"""


def text_indentation(text):
    """replaces ',', '?' and ':' with two new lines"""
    if not isinstance(text, str):
        """check if text is a string"""
        raise TypeError("text must be a string")
    i = 0

    while i < len(text) and text[i] == ' ':
        i += 1
    while i < len(text):
        print(text[i], end='')
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print('\n')
                while i < len(text) and text[i] == ' ':
                    i += 1
                    continue
        i += 1
