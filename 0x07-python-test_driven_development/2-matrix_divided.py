#!/usr/bin/python3
""" module with a function that divides a matrix """


def raise_type_error():
    """ helper function """
    s = "matrix must be a matrix (list of lists) of integers/floats"
    raise TypeError(s)


def matrix_divided(matrix, div):
    """ divide all elements of a matrix """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list()

    if not isinstance(matrix, list):
        raise_type_error()
    if not isinstance(matrix[0], list):
        raise_type_error()

    row_size = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise_type_error()
        if row_size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = list()
        for i in row:
            if not isinstance(i, (int, float)):
                raise_type_error()
            new = round((i / div), 2)
            if new in [float('inf'), -float('inf')]:
                new = 0.0
            new_row.append(new)
        new_matrix.append(new_row)
    return new_matrix
