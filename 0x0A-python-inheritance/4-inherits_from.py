#!/usr/bin/python3

"""A module that checks if object is an instance of a class."""


def inherits_from(obj, a_class):
    """This function returns True if the object is an instance of a 
    class that inherited from the specified class, otherwise false."""

    if issubclass(type(obj), a_class):
        return True
    return False 	
