#!/usr/bin/python3
""" divide a matrix."""


def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix."""
    for row in matrix:
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    length = matrix[0]
    for row in matrix:
        if len(row) != len(length):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    
    r row in matrix:
        for x in row:
            result = x / div	
            new_matrix.append(round(result, 2))
    return ([new_matrix])
