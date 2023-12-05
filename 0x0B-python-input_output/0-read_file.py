#!/usr/bin/python3
""" 0. Read file """


def read_file(filename=""):
    """
    read and print out contents of a file
    """
    with open(filename, encoding='utf-8') as fp:
        print(fp.read(), end="")
