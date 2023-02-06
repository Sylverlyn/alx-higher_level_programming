#!/usr/bin/python3
""" This module checks if an obj is an exact instance of a specified class."""


def is_same_class(obj, a_class):
    """returns True if an object is an exact instance of a class."""
    return type(obj) is a_class
