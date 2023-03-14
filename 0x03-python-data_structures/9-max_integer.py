#!/usr/bin/python3
def max_integer(my_list=[]):
    if not (my_list):
        return (None)
    largest = my_list[0]
    for m in my_list:
        if m > largest:
            largest = m
    return (largest)
