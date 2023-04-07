#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmatrix = []
    for i in range(len(matrix)):
        nmatrix.append([])

        for j in range(len(matrix[i])):
            nmatrix[i].append(matrix[i][j] ** 2)

    return nmatrix
