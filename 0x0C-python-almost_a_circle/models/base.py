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

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json representation of an object to a file

        Args:
            list_objs (list): list of objects
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode='w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dict = [i.to_dictionary() for i in list_objs]
                json_str = cls.to_json_string(list_dict)
                file.write(json_str)

    @staticmethod
    def from_json_string(json_string) -> list:
        """loads from a json string

        Args:
            json_string (str): json representation of list of objects

        Returns:
            list: list of dictionaries
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary) -> object:
        """creates an instance from dictionary description

        Returns:
            object: the newly created object
        """
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj = cls(1)

        obj.update(**dictionary)
        return (obj)

    @classmethod
    def load_from_file(cls) -> list:
        """load list of obj from file

        Returns:
            list: list of objs
        """
        filename = cls.__name__ + '.json'
        try:
            with open(filename, mode='r') as file:
                content = file.read()

            list_dict = Base.from_json_string(content)
            list_obj = [cls.create(**i) for i in list_dict]

            return list_obj
        except FileNotFoundError as e:
            return []
