#!/usr/bin/python3
"""Defines a function that writes a string to a file"""


def write_file(filename="", text="") -> int:
    """writes to a file

    Args:
        filename (str, optional): name the file to write to. Defaults to "".
        text (str, optional): the string to write to the file.
        Defaults to "".

    Returns:
        int: the number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
