#!/usr/bin/python3
"""
12. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    returns a list of list of integers conforming to
    Pascal's triangle
    """
    if n <= 0:
        return []
    outbound = []
    row = [1]
    for i in range(n):
        p = row[:] + [0]
        x1, x2 = 0, 1
        row = [1]
        for j in range(i):
            row.append(p[x1] + p[x2])
            x1 += 1
            x2 += 1
        outbound.append(row)
    return outbound
