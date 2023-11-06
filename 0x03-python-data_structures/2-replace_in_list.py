#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    my_list.pop(idx)
    my_list.insert(idx, element)
    return my_list

old_list = [1, 2, 3]
idx = 0 
element = 4

print(old_list)
print(replace_in_list(old_list, idx, element))
