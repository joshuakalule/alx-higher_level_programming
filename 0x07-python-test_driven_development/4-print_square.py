#!/usr/bin/python3
""" 3. Print square """


def print_square(size):
    """ prints a square with the character # """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be >= 0")
    if size < 0:
        raise ValueError("size must be >= 0")
    try:
        size = int(size)
    except (ValueError, OverflowError):
        size = 0
    for i in range(size):
        print("{}".format("#" * size))
