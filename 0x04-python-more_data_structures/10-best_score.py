#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = None
    key = None
    for k, v in a_dictionary.items():
        if not best:
            best = v
            key = k
            continue
        if v > best:
            key = k
    return key
