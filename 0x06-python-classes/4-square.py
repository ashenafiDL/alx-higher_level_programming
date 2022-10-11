#!/usr/bin/ptyhon3
"""This module defines a class called Square.
"""

class Square:
    """Represents a square with a size
    """

    def __init__(self, size=0):
        """Initializes a new square object with a size

        Args:
            size (int): the size of the sqaure. The size must be positive number
            (obviously)
        """
        self.size = size

    @property
    def size(self):
        """int: the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


    def area(self):
        """Computes the area of the square object

        Returns:
            The are of the current sqaure object
        """
        return (self.__size * self.__size)
