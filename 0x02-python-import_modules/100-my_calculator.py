#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

argc = len(argv)
if __name__ == "__main__":

    if (argc - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operations = {"+": add, "-": sub, "*": mul, "/": div}

    if argv[2] not in list(operations.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, argv[2], b, operations[argv[2]](a, b)))
