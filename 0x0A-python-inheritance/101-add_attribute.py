#!/usr/bin/python3
""" 13. Can I? """


def add_attribute(cls, attrib, value):
    """
    adds attributes if possible
    """
    if not hasattr(cls, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(cls, attrib, value)
