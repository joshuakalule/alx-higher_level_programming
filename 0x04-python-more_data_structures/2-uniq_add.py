#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    if not my_list:
        return 0
    done = []
    for i in my_list:
        if i not in done:
            done.append(i)
            sum += i
    return sum
