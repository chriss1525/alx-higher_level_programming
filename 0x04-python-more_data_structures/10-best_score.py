#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) is not dict or len(a_dictionary) == 0:
        return None
    biggest = list(a_dictionary.keys())[0]
    bignum = a_dictionary[biggest]
    for i, j in a_dictionary.items():
        if j > bignum:
            bignum = j
            biggest = i
    return biggest
