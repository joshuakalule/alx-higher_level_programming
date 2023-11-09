#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return my_list
    new = list()
    for i in my_list:
        _i = i
        if i == search:
            _i = replace
        new.append(_i)
    return new
