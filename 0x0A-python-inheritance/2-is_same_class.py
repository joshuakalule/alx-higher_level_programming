#!/usr/bin/python3
""" 2. Exact same object """


def is_same_class(obj, a_class):
    """
    checks if obj is exactly an instance of a_class
    """
    return type(obj) == a_class
