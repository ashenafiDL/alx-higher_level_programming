#!/usr/bin/python3
"""Defines a function that returns the list of available
attributes and methods of an obeject
"""


def lookup(obj) -> list:
    """returns a list of available attributes and methods os `obj`

    Args:
        obj (obj): an object

    Returns:
        list: a list containig all attributes and mthods of `obj`
    """
    return dir(obj)
