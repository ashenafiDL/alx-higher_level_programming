#!/usr/bin/python3
"""Defines a function that returns the JSON representation of an object"""

import json


def to_json_string(my_obj) -> str:
    """change a python objects to JSON equivalent

    Args:
        my_obj (any): python object

    Returns:
        str: JSON representation of `my_obj`
    """
    return json.dumps(my_obj)
