#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerator = sum(list(map(lambda x: x[0]*x[1], my_list)))
    denominator = sum([x[1] for x in my_list])
    return numerator/denominator
