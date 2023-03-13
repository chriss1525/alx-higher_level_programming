#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if my_string[i] != 'c' & my_string[i] != 'C':
            print("{}".format(my_string[i]))
