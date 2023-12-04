#!/usr/bin/python3
""" 1. My list """


class MyList(list):
    """ a class that inherits from list """

    def print_sorted(self):
        """ prints the list but sorted in ascending order """
        s_list = sorted(self)
        print(s_list)
