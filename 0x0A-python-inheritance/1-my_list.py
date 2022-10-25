#!/usr/bin/python3
"""Defines a class `MyList` that inherits from `list`

and a function that prints the sorted list
"""


class MyList(list):
    """A class that inherits from the `list` class
    and prints the list in ascending order
    """

    def print_sorted(self) -> None:
        """prints a list in ascending sorted order
        """
        list_copy = super().copy()
        print(sorted(list_copy))
