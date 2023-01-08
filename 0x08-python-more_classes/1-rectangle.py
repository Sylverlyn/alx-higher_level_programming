#!/usr/bin/python3

class Rectangle:
    """Represent a rectangle.

    Args:
        width (int): The width of the new rectangle.
        height (int): The height of the new rectangle.
    """
    def __init__(self, width=0, height=0):
        """initializes a new rectangle."""

        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be an integer")
        self.__height = value
