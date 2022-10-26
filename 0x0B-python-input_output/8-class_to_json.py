#!/usr/bin/python3
"""defines a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj) -> dict:
    """class to json

    Args:
        obj (any): object

    Returns:
        dict: dictinary description of `obj`
    """
    return obj.__dict__
