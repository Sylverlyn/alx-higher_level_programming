#!usr/bin/python3
"""class to object."""
import json


def class_to_json(obj):
    """returns data structure for JSON
    serialization of object."""
    return json.dumps(obj.__dict__.copy())
