#!/usr/bin/python3
def search_replace(my_list, search, replace):
    rlist = []
    for i in my_list:
        if i == search:
            rlist.append(replace)
        else:
            rlist.append(i)
    return rlist
