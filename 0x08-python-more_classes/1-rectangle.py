#!/usr/bin/python3
"""defines a class Rectangle."""


class Rectangle:
    """creates a class Rectangle."""
    def __init__(self, width=0, height=0):
        """initialises the Rectangle object."""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieves the current width of the attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the new value of the attribute."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the current height of the attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the new value of the attribute."""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
