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
