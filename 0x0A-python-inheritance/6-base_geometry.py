#!/usr/bin/python3
"""Defines an empty class called `BaseGeometry`"""


class BaseGeometry():
    """Defines a method that throws an Exception
    """

    def area(self) -> None:
        """Throws an exception with the message

        `area() is not implemented`
        """
        raise Exception("area() is not implemented")
