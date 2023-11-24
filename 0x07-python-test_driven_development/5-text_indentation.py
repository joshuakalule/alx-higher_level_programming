#!/usr/bin/python3
""" 4. Text indentation """


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters:
    ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special = ['.', '?', ':']
    spaces = [' ', '\t']
    prev = None
    string = ""
    for c in text:
        if c == '\n':
            if prev in spaces:
                tmp = prev
                while tmp in spaces:
                    string = string[:-1]
                    tmp = string[-1]
            string += c
        elif c in special:
            string += "{}\n\n".format(c)
            prev = '\n'
            continue
        elif c in spaces:
            if prev == '\n':
                continue
            else:
                string += c
        else:
            string += c
        prev = c
    print(string, end="")
    return string
