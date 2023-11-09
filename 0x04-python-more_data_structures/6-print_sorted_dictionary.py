#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return None
    keys = list(a_dictionary.keys())
    keys.sort()
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
