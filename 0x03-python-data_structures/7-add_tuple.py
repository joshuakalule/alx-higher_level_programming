#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ans = [0, 0]
    for t in (tuple_a, tuple_b):
        for n in range(2):
            if not t or n > len(t) - 1:
                break
            ans[n] += t[n]
    return tuple(ans)
