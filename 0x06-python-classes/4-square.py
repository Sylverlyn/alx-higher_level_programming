#!/usr/bin/python3
"""defines a square."""


class Square:
    """creates a class."""
    def __init__(self, size=0):
        """initializes an instance."""

        self.__size = size

    def area(self):
        """computes and returns area of the current square."""
        return self.__size**2

    @property
    def size(self):
        """retrieves the current size of the argument."""
        return self.__size

    @size.setter
    def size(self, value):
        """sets/assigns a new value to the attribute."""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
