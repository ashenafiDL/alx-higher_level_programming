#!/usr/bin/python3
"""Defines a function that returns an object represented by a JSON string"""

import json


def from_json_string(my_str) -> any:
    """returns an object represented by a JSON string

    Args:
        my_str (str): JSON string

    Returns:
        any: a python data structure represented by `my_str`
    """
    return json.loads(my_str)
