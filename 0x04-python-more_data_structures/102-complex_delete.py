#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return dict()
    trash = []
    for k, v in a_dictionary.items():
        if v == value:
            trash.append(k)
    for key in trash:
        del a_dictionary[key]
    return a_dictionary
