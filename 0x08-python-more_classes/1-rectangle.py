#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle():
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object with width and height

        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """The width of the rectangle.

        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self) -> int:
        """The height of the rectangle.

        Returns:
            int: height
        """
        return self.__height

    @width.setter
    def height(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
