#!/usr/bin/python3
"""Defines a function that checks

    - if an object is an instance of,
    - or if the object is an instance of a class that inherited from,
    the specified class
"""


def is_kind_of_class(obj, a_class) -> bool:
    """checks

    - if an object is an instance of,
    - or if the object is an instance of a class that inherited from,
    the specified class

    Args:
        obj (obj): an object
        a_class (class): a class

    Returns:
        bool: True if `obj`
        - is an instance of,
        - or if `obj` is an instance of a class that inherited from,
        `a_class`

        otherwise False
    """
    return isinstance(obj, a_class)
