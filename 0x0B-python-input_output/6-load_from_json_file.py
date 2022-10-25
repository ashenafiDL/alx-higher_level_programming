#!/usr/bin/python3
"""Defines a function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename) -> any:
    """creates an Object from a JSON file

    Args:
        filename (str): name of the file

    Returns:
        any: an object based on JSON string
    """
    with open(filename) as file:
        return json.load(file)
