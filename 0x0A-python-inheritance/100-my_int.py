#!/usr/bin/python3
"""Defines a class `MyInt` that inherits from `int`
"""


class MyInt(int):
    """A class that inherits from `int`

    and FYI MyInt is a rebel:
    becareful when dealing with `==` and `!=` operators
    """

    def __eq__(self, value) -> bool:
        """overrides `==` with `!=`

        Args:
            value (int): integer

        Returns:
            bool: self != value
        """
        return self.real != value

    def __ne__(self, value) -> bool:
        """overrides `!=` with `==`

        Args:
            value (int): integer

        Returns:
            bool: self == value
        """
        return self.real == value
