#!/usr/bin/python3
"""Defines a function that adds a new attribute to an object
if it is possible
"""


def add_attribute(object, attribute, value):
    """adds attribute to an object

    Args:
        object (oany): object
        attribute (str): name attribute
        value (any): value of attribute
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attribute, value)
