#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    n = len(sentence)
    if n == 0:
        first = None
    else:
        first = sentence[0]
    return (n, first)
