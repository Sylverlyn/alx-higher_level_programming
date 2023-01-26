#!/usr/bin/python3
"""defines a square."""


class Square:
    """creates a class."""
    def __init__(self, size=0, position=(0, 0)):
        """initializes an instance."""

        self.__size = size
        self.__position = position

    def area(self):
        """computes and returns area of the current square."""
        return self.__size**2

    @property
    def position(self):
        """retrieves the current position of the attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive intergers")
        else:
            self.__position = value

    @property
    def size(self):
        """retrieves the current size of the attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """sets/assigns a new value to the attribute."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """prints the square character # to the stdout"""
        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" "*self.__position[0], end="")
                print("#"*self.__size)
        else:
            print("\n")
