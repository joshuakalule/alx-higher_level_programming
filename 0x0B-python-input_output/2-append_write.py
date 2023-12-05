#!/usr/bin/python3
""" 2. Append to a file """


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file
    """
    with open(filename, 'a', encoding='utf-8') as fp:
        return fp.write(text)
