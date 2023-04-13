#!/usr/bin/python3
"""this module defines save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """
    args: my_object object to be saved
    filename, where object is saved
    write an object to a text file using json representation
    """
    import json

    with open(filename, "w") as f:
        json.dump(my_obj, f)
