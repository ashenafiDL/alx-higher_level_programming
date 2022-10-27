#!/usr/bin/python3
"""Defines a function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename (str, optional): name of the file. Defaults to "".
        search_string (str, optional): the string to search. Defaults to "".
        new_string (str, optional): the new string to append. Defaults to "".
    """
    new_text = ""
    with open(filename, mode='r') as file:
        for line in file:
            new_text += line
            if search_string in line:
                new_text += new_string

    with open(filename, mode='w') as file:
        file.write(new_text)
