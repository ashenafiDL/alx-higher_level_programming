#!/usr/bin/python3
"""Defines a class `Square` that inherits from `Rectangle` class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines a sqaure"""

    def __init__(self, size) -> None:
        """initializes a `Square` instance

        Args:
            size (int): length size of a square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self) -> int:
        """calculates area of `Square` instance

        Returns:
            int: area of square
        """
        return self.__size**2

    def __str__(self) -> str:
        """makes a `Square` instance printable

        Returns:
            str: `Square` instance description in the form of:
            `[Square] <width>/<height>`
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
