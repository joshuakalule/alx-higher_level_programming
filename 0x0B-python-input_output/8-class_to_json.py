#!/usr/bin/python3
"""
8. Class to JSON
"""


def class_to_json(obj):
    """
    returns a dict description with simple data structure
    """
    return obj.__dict__
