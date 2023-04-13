#!/usr/bin/python3
"""this module defines load_from_json_file"""


def load_from_json_file(filename):
    """create an object from a json file"""
    with open(filename) as f:
        return json.load(f)
