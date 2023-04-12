#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for i in a_dictionary.items():
        new_dict.update({i[0]: i[1] * 2})
    return new_dict
