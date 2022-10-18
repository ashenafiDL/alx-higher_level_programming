#!/usr/bin/python3
"""Defines a function that prints a square using a #"""


def print_square(size) -> None:
    """prints a square with the character #

    Args:
        size (int): the length/width of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for height in range(size):
        [print("#", end='') for width in range(size)]
        print("")
