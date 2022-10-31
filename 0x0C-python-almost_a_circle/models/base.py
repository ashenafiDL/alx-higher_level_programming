#!/usr/bin/python3
"""Defines a base class for all the future classes"""
import json


class Base():
    """This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all future classes
    and to avoid duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """Initializes a `Base` instance

        Args:
            id (int, optional): The ID of the new `Base` instance.
            Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries) -> str:
        """turns list of dictionaries into JSON representation

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            str: JSON representation of `list_dictionaries`
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)
