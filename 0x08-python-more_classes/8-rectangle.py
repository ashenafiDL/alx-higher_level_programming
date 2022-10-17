#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle():
    """Defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle object with width and height

        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self) -> int:
        """The width of the rectangle.

        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self) -> int:
        """The height of the rectangle.

        Returns:
            int: height
        """
        return self.__height

    @width.setter
    def height(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self) -> int:
        """Returns the area of a rectangle

        Returns:
            int: area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self) -> int:
        """Returns the perimeter of the rectangle

        Returns:
            int: perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self) -> str:
        """print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for h in range(self.__height):
            rectangle.append(self.__width * str(self.print_symbol))

        return "\n".join(rectangle)

    def __repr__(self) -> str:
        """returns string representation of Rectangle object
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor for Rectangle objects"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two Rectangle objects

        Args:
            rect_1 (Rectangle): the first rectangle
            rect_2 (Rectangle): the second rectangle

        Returns:
            Rectangle: the biggest rectangle based on the area
            or `rect_1` if both have the same are value
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
