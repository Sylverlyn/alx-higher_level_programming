#!/usr/bin/python3
"""A module that checks if object is a subclass."""


def inherits_from(obj, a_class):
    """This function returns True if the object is an instance of a class
    that inherited from the specified class."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
