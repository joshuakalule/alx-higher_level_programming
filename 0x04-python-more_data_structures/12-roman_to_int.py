#!/usr/bin/python3
d = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not isinstance:
        return 0
    num = 0
    prev = 0
    for c in roman_string:
        n = d[c]
        if n > prev:
            num += n - 2*prev
        else:
            num += n
        prev = n
    return (num)
