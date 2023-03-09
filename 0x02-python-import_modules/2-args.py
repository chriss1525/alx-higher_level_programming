#!/usr/bin/python3
from sys import argv
argc = len(argv)
if __name__ == '__main__':
    index = 1
    if argc == 1:
        print("{} arguments.".format(argc - 1))
    elif argc == 2:
        print("{} argument:".format(argc - 1))
        print("1: {}".format(argv))
    elif argc > 2:
        print("{} arguments:".format(argc - 1))
        while (index < argc):
            print("{}: {}".format(index, argv[index]))
            index += 1
