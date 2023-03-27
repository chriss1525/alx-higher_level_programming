#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    len = 0
    for i in range(sx):
        try:
            print("{:d}".format(my_list[i]), end="")
            len += 1
        except Exception:
            continue
    print("")
    return len
