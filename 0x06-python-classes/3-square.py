#!/usr/bin/python3
"""
    class implementation task 3
"""


class Square:
    """ class that defines a square

    Attributes:
        size (int): size of the square
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """int: getter method for size"""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Area of the square """
        return self.__size ** 2
