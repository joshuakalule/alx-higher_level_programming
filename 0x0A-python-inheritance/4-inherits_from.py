#!/usr/bin/python3
""" 4. Only sub class of """


def inherits_from(obj, a_class):
    """ is subclass """
    return isinstance(obj, a_class) and type(obj) != a_class
