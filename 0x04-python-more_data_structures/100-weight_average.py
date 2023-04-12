#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score = 0
    weight = 0
    for i in my_list:
        score += i[0] * i[1]
        weight += i[1]
    average = float(score / weight)
    return average
