#!/usr/bin/python3
"""Defines a function for greetings"""


from unicodedata import name


def say_my_name(first_name, last_name="") -> None:
    """a function that prints a text in the following format

    My name is <first_name> <last_name>

    Args:
        first_name (str): firt name
        last_name (str, optional): last name. Defaults to "".
    """
    err_msg = "{name} must be a string"

    if not isinstance(first_name, str):
        raise TypeError(err_msg.format(name='first_name'))
    if not isinstance(last_name, str):
        raise TypeError(err_msg.format(name='last_name'))

    print("My name is {} {}".format(first_name, last_name))
