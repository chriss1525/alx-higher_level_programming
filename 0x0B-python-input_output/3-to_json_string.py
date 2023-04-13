#!/usr/bin/python3
""" this module defines to_json_string"""


def to_json_string(my_obj):
    """returns the JSON representation of an object(string)"""
    import json

    result = json.dumps(my_obj)
    return result
