#!/usr/bin/python3
"""Defines a function that checks
if an object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class) -> bool:
    """checks is `obj` is an instance of `a_class`

    Args:
        obj (obj): an object
        a_class (class): a class

    Returns:
        bool: True if `obj` is exactly an instance of `a_class`
        otherwise False
    """
    return (type(obj) is a_class)
