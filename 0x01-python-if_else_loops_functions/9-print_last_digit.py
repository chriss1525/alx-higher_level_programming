#!/usr/bin/python3
def print_last_digit(number):
    ld = abs(number) % 10
    print(f'{ld:d}', end='')
    return (ld)
