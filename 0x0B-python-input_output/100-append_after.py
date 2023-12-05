#!/usr/bin/python3
"""
13. Search and update
inserts a line of text to a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inset new_string every after search_string in filename
    """
    found = 0
    base = ""
    if len(search_string) == 0:
        return
    string = str()
    with open(filename, 'r', encoding='utf-8') as fp:
        while (line := fp.readline()):
            string += line
            if search_string in line:
                string += new_string

    with open(filename, 'w', encoding='utf-8') as fp:
        fp.writelines(string)
