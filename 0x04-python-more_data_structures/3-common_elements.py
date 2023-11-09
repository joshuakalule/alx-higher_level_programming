#!/usr/bin/python3
def common_elements(set_1, set_2):
    if not set_1 or not set_2:
        return []
    s1 = set(set_1)
    s2 = set(set_2)
    return list(s1.intersection(s2))
