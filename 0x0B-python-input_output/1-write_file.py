#!/usr/bin/python3
""" 1. Write to a file """


def write_file(filename="", text=""):
    """
    writes to a text file (UTF8)
    """
    with open(filename, 'w', encoding='utf-8') as fp:
        return fp.write(text)
