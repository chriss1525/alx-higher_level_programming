#!/usr/bin/python3
"""this module defines text_indentation"""


def text_indentation(text):
    """replaces ',', '?' and ':' with two new lines"""
    if not isinstance(text, str):
        """check if text is a string"""
        raise TypeError("text must be a string")
    print("{}".format(text)
          .replace('. ', '\n\n')
          .replace('? ', '\n\n')
          .replace(': ', '\n\n'))
