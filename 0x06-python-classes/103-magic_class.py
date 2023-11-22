#!/usr/bin/python3
""" module Documentation """

import math


class MagicClass:
    """ implement magic class

    Attributes:
        radius (int): radius
    """
    def __init__(self, radius=0):
        self._MagicClass__radius = 0
        if isinstance(radius, int) or isinstance(radius, float):
            self._MagicClass__radius = radius
        else:
            raise TypeError("radius must be a number")

    def area(self):
        """ area of the circle """
        return math.pi * (self._MagicClass__radius ** 2)

    def circumference(self):
        """ circumference of a circle """
        return 2 * math.pi * self._MagicClass__radius
