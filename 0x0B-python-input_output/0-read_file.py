#!/usr/bin/python3
"""Defines a function that reads a text file and prints it to stdout"""


def read_file(filename="") -> None:
    """reads contents of a file

    Args:
        filename (str, optional): name of the file to be opened.
        Defaults to "".
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read())
