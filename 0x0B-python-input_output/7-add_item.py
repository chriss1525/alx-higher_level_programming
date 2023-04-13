#!/usr/bin/python3
"""add all aruments and save them to a file"""

import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


sys.argv.pop(0)
try:
    arguments = load_from_json_file("add_item.json")
    if arguments is None:
        save_to_json_file(sys.argv, "add_item.json")
    else:
        arguments.extend(sys.argv)
        save_to_json_file(arguments, "add_item.json")
except FileNotFoundError:
    save_to_json_file(sys.argv, "add_item.json")
