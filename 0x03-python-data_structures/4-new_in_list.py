#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return []
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    new_list = my_list.copy()
    new_list.pop(idx)
    new_list.insert(idx, element)
    return new_list
