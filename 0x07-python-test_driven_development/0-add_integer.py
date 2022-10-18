#!/usr/bin/python3
"""Defines a function that add two integers

The function accepts two ints or floats and return their sum
otherwise raise a TypeError if invalid argument is passed
"""


def add_integer(a, b=98) -> int:
    """Returns the sum of a and b

    Args:
        a (int/float): the first number
        b (int/float, optional): the second number. Defaults to 98.

    Returns:
        (int): the sum of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
