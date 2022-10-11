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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
