#!/usr/bin/python3
"""Defines a function that checks if an object is
dirctly/indirctly inherited from the specified class
"""


def inherits_from(obj, a_class) -> bool:
    """checks if an object is
    dirctly/indirectly inherited from the specified class

    Args:
        obj (obj): an object
        a_class (class): a class

    Returns:
        bool: True if `obj` is an instance of a class that inherited
        (directly or indirectly) from `a_class`
        otherwise False
    """
    return issubclass(obj.__class__, a_class) and type(obj) is not a_class
