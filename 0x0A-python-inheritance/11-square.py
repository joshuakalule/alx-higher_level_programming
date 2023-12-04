#!/usr/bin/python3
""" 11. Square #2 """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square implementation of Rectangle
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square] {0}/{0}".format(self.__size)
