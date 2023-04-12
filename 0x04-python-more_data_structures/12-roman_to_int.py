#!/usr/bin/python3
def roman_to_int(roman_string):
    rnumbers = {'I': 1, 'V': 5, 'X': 10,
                'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    if not roman_string or type(roman_string) != str:
        return 0
    for j in range(len(roman_string)):
        if j > 0 and rnumbers[roman_string[j]] > rnumbers[roman_string[j - 1]]:
            sum += rnumbers[roman_string[j]] - 2 * \
                rnumbers[roman_string[j - 1]]
        else:
            sum += rnumbers[roman_string[j]]
    return sum
