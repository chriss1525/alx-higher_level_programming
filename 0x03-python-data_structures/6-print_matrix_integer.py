#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for i in range(len(list)):
            print("{:d}".format(list[i]), end="")
            if i < len(list) - 1:
                print(" ", end="")
        print("")
