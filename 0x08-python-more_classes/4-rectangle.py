#!/usr/bin/python3
"""Defines the area and perimeter of a rectangle."""


class Rectangle:
    """creates a rectangle."""

    def __init__(self, width=0, height=0):
        """initializes width and height of a rectangle."""

        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width of the rectangle."""
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
        """gets the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must >=0")
        self.__height = value

    def area(self):
        """returns the ares of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = ""
        for i in range(self.__height):
            for j in range(self.__width):

                rec += "#"
            rec += '\n'
        return (rec[:-1])

    def __repr__(self):
        """return a string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height)"
