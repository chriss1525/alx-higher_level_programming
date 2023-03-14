#!/usr/bin/python3
def max_integer(my_list=[]):
    l = my_list[0]
    for m in my_list:
        if m > l:
            l = m
    return (l)
