#!/usr/bin/python3
"""This module defines a class called Square.
"""


class Square:
    """Represents a square with a size
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square object with a size

        Args:
            size (int): the size of the sqaure.
            The size must be positive number (obviously)
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """tuple: the coordinates of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Computes the area of the square object

        Returns:
            The are of the current sqaure object
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the character #
        """

        if self.__size == 0:
            print("")
        else:
            # first print empty lines for the amount of the y coordinate
            for y in range(0, self.__position[1]):
                print("")

            for height in range(0, self.__size):
                # before printing the row first print " "
                # for the amount of x coordinate
                for x in range(0, self.__position[0]):
                    print(' ', end='')
                for width in range(0, self.__size):
                    print("#", end='')
                print("")