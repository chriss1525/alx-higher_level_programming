#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)
    mid = len(list_of_integers) // 2
    if (mid == 0 or list_of_integers[mid] > list_of_integers[mid - 1]) and \
            (mid == len(list_of_integers) - 1 or
             list_of_integers[mid] > list_of_integers[mid + 1]):
        return list_of_integers[mid]

    if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    return find_peak(list_of_integers[mid + 1:])
