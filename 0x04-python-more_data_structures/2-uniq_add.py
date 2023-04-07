#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    sum = 0
    for i in my_list:
        if i not in uniq:
            sum += i
            uniq.append(i)
    return sum
