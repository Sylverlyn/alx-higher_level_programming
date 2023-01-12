#!/usr/bin/python3
"""Defines a rectangle."""


class Rectangle:
    """creates a rectangle."""

    def __init__(self, width=0, height=0):
        """initializes the attributes of a rectangle."""

        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """gets the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of a rectangle."""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must >= 0")
        self.__height = height
