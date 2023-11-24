#!/usr/bin/python3
""" 7. Lazy matrix multiplication """
import numpy as np

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
        Fail: < 0 (check 'error_dict' for details)
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
        m_len = len(m)
        for i in m:
            if not isinstance(i, (int, float)):
                pass
    return (0)


def lazy_matrix_mul(m_a, m_b):
    """ multiplies 2 matrices by using the module NumPy """
    if isinstance(m_a, str) or isinstance(m_b, str):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    m_a = np.array(m_a)
    m_b = np.array(m_b)
    return (np.dot(m_a, m_b))
