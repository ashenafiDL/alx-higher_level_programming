#!/usr/bin/python3
"""A LockedClass that will only allow
an attribute name called `first_name` to be created
"""


class LockedClass():
    """Only an attribute called `first_name` can be created in this class"""

    __slots__ = ['first_name']
