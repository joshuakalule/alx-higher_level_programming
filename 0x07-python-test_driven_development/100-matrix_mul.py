#!/usr/bin/python3
""" 6. Matrix multiplication """

error_dict = {
    -1: "matrix must be a list",
    -2: "matrix must be a list of lists",
    -3: "matrix can't be empty",
    -4: "each row of matrix must be of the same size",
    -5: "matrix should contain only integers or floats"
}


def check_list(matrix):
    """
    check if 'matrix' is a list of lists of integers

    Returns:
        True: 0
        Fail:
            -1: matrix must be a list
            -2: matrix must be a list of lists
            -3: matrix can't be empty
            -4: each row of matrix must be of the same size
            -5: matrix should contain only integers or floats
    """
    if matrix in ([[]], []):
        return (-3)
    if not isinstance(matrix, list):
        return (-1)
    try:
        m_len = len(matrix[0])
    except TypeError:
        return (-2)
    for m in matrix:
        if not isinstance(m, list):
            return (-2)
        if m_len != len(m):
            return (-4)
        m_len = len(m)
        for i in m:
            if not isinstance(i, (int, float)):
                return (-5)
    return (0)


def matrix_mul(m_a, m_b):
    """ multiplies 2 matrices """

    if (e := check_list(m_a)) != 0:
        raise TypeError(error_dict[e].replace('matrix', 'm_a'))
    if (e := check_list(m_b)) != 0:
        raise TypeError(error_dict[e].replace('matrix', 'm_b'))
    cols_a = len(m_a[0])
    cols_b = len(m_b[0])
    rows_a = len(m_a)
    rows_b = len(m_b)
    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    mul = list()
    for r in range(rows_a):
        row = list()
        for c in range(cols_b):
            zipped = zip(m_a[r], [x[c] for x in m_b])
            result = sum([x[0] * x[1] for x in zipped])
            row.append(result)
        mul.append(row)
    return mul
