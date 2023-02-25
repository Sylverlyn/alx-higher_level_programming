#!/usr/bin/python3
"""module inherits from the Base class"""
from models.base import Base


class Rectangle(Base):
    """A class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialises the function"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets the current value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets new value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets the current value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets new value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets the current value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets new value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets the current value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets new value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area value of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.y):
            print()
        for row in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """returns string representation of the class"""
        return (f"[{self.__class__.__name__}], ({self.id}) {self.x}/{self.y}-{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """assigns each argument to a corresponding attribute"""
        #if args is not None and len(args) is not 0:
        attributes = ("id", "width", "height", "x", "y")
        if args:           
            for index, value in enumerate(args):
                setattr(self, attributes[index], value)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of the object."""
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}            
