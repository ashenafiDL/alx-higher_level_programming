#!usr/bin/python3
"""Defines a function that writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename) -> None:
    """writes an Objects to a text file, using JSON representation

    Args:
        my_obj (any): python object
        filename (str): name of file to write to
    """
    with open(filename, mode='w', encoding='utf8') as file:
        json.dump(my_obj, file)
