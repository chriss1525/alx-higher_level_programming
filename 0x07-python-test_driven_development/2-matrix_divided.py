#!/usr/bin/python3
"""
matrix_divided

divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Returns value of divided matrix
    >>>matrix_divided()
    """

    result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    def check_types(matrix, types):
        """checks if matrix is a list of lists"""
        for list in matrix:
            for element in list:
                if not isinstance(element, types):
                    raise TypeError("matrix must be a matrix (list of lists)"
                                    "of integers/floats")

    def check_size(matrix, size):
        """checks if items in matrix are the same size"""
        for array in matrix:
            if len(array) != size:
                raise TypeError("Each row of the matrix"
                                " must have the same size")

    def check_div(div):
        """Checks if the div is a float or int and if div is not zero """
        if not isinstance(div, (float, int)):
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")

    check_types(matrix, (int, float))
    check_size(matrix, len(matrix[0]))
    check_div(div)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            """round off answer to 2 decimal places"""
            result[i][j] = round(matrix[i][j] / div, 2)
    return result
