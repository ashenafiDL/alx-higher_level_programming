#!/usr/bin/python3
"""Defines a function that appends a string to a file"""


def append_write(filename="", text="") -> int:
    """appends a string to a file

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): string to append to the file. Defaults to "".

    Returns:
        int: number of characters appended
    """
    with open(filename, mode='a', encoding='utf8') as file:
        return file.write(text)
