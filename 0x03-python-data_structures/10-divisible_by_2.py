#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    copy = []

    for i in my_list:
        if i % 2:
            copy.append(True)
        else:
            copy.append(False)
    return (copy)