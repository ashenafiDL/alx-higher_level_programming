#!/usr/bin/python3
"""Defines a MagicClass
"""
import math


class MagicClass:
    """A magic class for a circle

    Raises:
        TypeError: if the radius is not an int or float
    """

    def __init__(self, radius=0):
        """initializes a MagicClass objects

        Args:
            value (float or int): radius of a circle
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area of a circle

        Returns:
            float: area of the circle
        """
        return self.__radius**2 * math.pi

    def circumference(self):
        """Calculates the circumference of a circle

        Returns:
            float: circumference of a circle
        """
        return 2 * math.pi * self.__radius
