#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if not set_1:
        return list(set(set_2))
    if not set_2:
        return list(set(set_1))
    s1 = set(set_1)
    s2 = set(set_2)
    union = s1.union(s2)
    inter = s1.intersection(s2)
    return list(union.difference(inter))
