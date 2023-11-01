#!/usr/bin/python3
def remove_char_at(str, n):
    out = ''
    for i in range(len(str)):
        if i != n:
            out += str[i]
    return out
