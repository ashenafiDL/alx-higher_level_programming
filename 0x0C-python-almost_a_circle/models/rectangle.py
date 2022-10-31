#!/usr/bin/python3
"""Defines a class that defines a rectangle"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        """instantiation of Rectangle instance

        Args:
            width (any): width of the rectangle
            height (any): height of the rectangle
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordinate. Defaults to 0.
            id (any, optional): id of the rectangle instance. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """X coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self) -> int:
        """calculates the area of a rectangle

        Returns:
            int: area of rectangle
        """
        return self.__height * self.__width

    def display(self):
        """Prints a `Rectangle instance with the character '#'`
        """
        [print("") for _ in range(self.__y)]
        for _ in range(self.__height):
            [print(" ", end="") for _ in range(self.__x)]
            [print("#", end="") for _ in range(self.__width)]
            print("")

    def __str__(self) -> str:
        """Makes `Rectangle` instance printable"""
        msg = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.height)
        return msg

    def update(self, *args, **kwargs) -> None:
        """Update a rectangle instance using `*args` and `**kwargs`"""
        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.width = arg
                elif index == 2:
                    self.height = arg
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg
                index += 1
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self) -> dict:
        """Return dictionary representation of rectangle instance"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
