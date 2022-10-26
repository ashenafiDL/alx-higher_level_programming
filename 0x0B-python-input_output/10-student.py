#!/usr/bin/python3
"""A class that defines a student"""


class Student():
    """A class that defines a student
    """

    def __init__(self, first_name, last_name, age) -> None:
        """initialize a `Student` instance

        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None) -> dict:
        """gets dictionary representation of `Student` instance

        Args:
            attrs (list, optional): list of attributes to get.
            Defaults to None.
        Returns:
            dict: dictionary representation of `Student` instance
        """
        if type(attrs) is list and all(type(item) for item in attrs):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
