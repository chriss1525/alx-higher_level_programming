#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    argc = len(argv)
    t_args = 0
    for index in range(argc - 1):
       t_args += int(argv[index + 1])
    print("{}".format(t_args))
