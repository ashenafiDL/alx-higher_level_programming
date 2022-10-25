#!/usr/bin/python3
"""Defines a class `Rectangle` that inherits from `BaseGeometry`
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle based on `BaseGeometry` class"""

    def __init__(self, width, height) -> None:
        """initializes a `Rectangle` instance

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self) -> int:
        """calculats area of rectangle

        Returns:
            int: area of rectangle
        """
        return self.__width * self.__height

    def __str__(self) -> str:
        """makes a `Rectangle` instance printable

        Returns:
            str: `Rectangle` instance description in the form of:
            `[Rectangle] <width>/<height>`
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
