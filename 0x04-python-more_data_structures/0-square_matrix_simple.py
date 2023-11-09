#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return []
    out = []
    for row in matrix:
        _row = list()
        for i in row:
            _row.append(i**2)
        out.append(_row)
    return (out)
