#!/usr/bin/python3
"""this module defines from_json_string"""


def from_json_string(my_str):
    """return an object represented by a JSON string"""
    import json

    result = json.loads(my_str)
    return (result)
