#!/usr/bin/python3
"""module defines a square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialises the class attributes."""
        super().__init__(size, size, x, y, id )
        
    def __str__(self):
        """returns string representation of square object"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.size}")
    
    @property
    def size(self):
       """returns the size"""
       return self.width

    @size.setter
    def size(self, value):
        """sets the new size"""
        self.width = value
        self.height = value    
    
    def update(self, *args, **kwargs):
        """assigns each argument to corresponding attribute"""
        #attributes = ("id", "size", "x","y")
        if args:
            attributes = ("id", "size", "x", "y")          
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
       """returns the dictionary representation of the object."""
       return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
