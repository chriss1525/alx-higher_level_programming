#!/usr/bin/python3
"""this module defines load_from_json_file"""


def load_from_json_file(filename):
    """create an object from a json file"""
    import json

    with open(filename) as file:
        return json.load(file)
