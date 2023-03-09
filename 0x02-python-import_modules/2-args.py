#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    argc = len(argv)
    index = 1
    if argc == 1:
        print("{} arguments.".format(argc - 1))
    elif argc == 2:
        print("{} argument:".format(argc - 1))
    else:
        print("{} arguments:".format(argc - 1))
        while index < argc:
            print("{}: {}".format(index, argv[index]))
            index += 1
