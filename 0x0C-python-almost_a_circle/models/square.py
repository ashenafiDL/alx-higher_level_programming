#!/usr/bin/python3
"""Defines a `Square` class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square"""

    def __init__(self, size, x=0, y=0, id=None) -> None:
        """initialize a `Square` instance

        Args:
            size (int): size of the square
            x (int, optional): x coordinate of the square. Defaults to 0.
            y (int, optional): y coordinate of the square. Defaults to 0.
            id (any, optional): id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """Makes `Square` instance printable

        Returns:
            str: description of square instance
        """
        msg = "[Square] ({}) {}/{} - {}".format(self.id,
                                                super().x, self.y, self.width)
        return msg

    @property
    def size(self) -> int:
        """The side length of the square"""
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the square instance by using `*args` and `**kwargs`"""
        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
                index += 1
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self) -> dict:
        """Returns the dictionary representation of square instance"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
