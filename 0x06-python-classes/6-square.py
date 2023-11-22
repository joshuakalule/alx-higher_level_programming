#!/usr/bin/python3
""" class implementation task 3 """


class Square:
    """ class that defines a square

    Attributes:
        size (int): size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def position(self):
        """tuple: position"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(map(lambda x: isinstance(x, int) and x >= 0, value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """int: getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Area of the square """
        return self.__size ** 2

    def my_print(self):
        """ Print Square """
        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print("{}".format(" " * self.__position[0]), end="")
            print("{}".format("#" * self.__size))
