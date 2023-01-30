#!/usr/bin/python3
"""defines a class Rectangle."""


class Rectangle:
    """creates a class Rectangle."""
    def __init__(self, width=0, height=0):
        """initialises the Rectangle object."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the current width of the object."""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the new value of the object."""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """retrieves the current height of the object."""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the new value of the object."""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """gets the area of the Rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """gets the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__height + self.__width)

    def __str__(self):
        """gets the string representation of the object."""
        if self.__width == 0 or self.__height == 0:
            return ""
        Rect = ""
        for row in range(self.__height):
            for colm in range(self.__width):
                Rect += "#"
            Rect += '\n'
        return Rect[:-1]

    def __repr__(self):
        """returns a string representation that can recreate a new object."""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """deletes an instance of Rectangle."""
        print("Bye rectangle...")
