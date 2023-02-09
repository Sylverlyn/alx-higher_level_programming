#!/usr/bin/python3
"""class to object."""


def class_to_json(obj):
    """returns data structure for JSON
    serialization of object."""
    return obj.__dict__
