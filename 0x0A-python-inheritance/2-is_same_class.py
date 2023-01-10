#!/usr/bin/python3

"""This method checks if an obj is an instance of a class."""


def is_same_class(obj, a_class):
    """This  function that returns True if the object is exactly
    an instance of the specified class ; otherwise False."""

    if isinstance(obj, a_class):
        return True
    return False
