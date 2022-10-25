#!/usr/bin/python3
"""Defines an empty class called `BaseGeometry`"""


class BaseGeometry():
    """Defines a method that throws an Exception
    and a function that validates integers
    """

    def area(self) -> None:
        """Throws an exception with the message

        `area() is not implemented`
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value) -> None:
        """validates integers

        Args:
            name (str): the name of `value`
            value (int): an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
