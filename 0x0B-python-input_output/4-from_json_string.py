#!/usr/bin/python3
""" module that returns JSON string to object"""
import json


def from_json_string(my_str):
    """ function that returns an object represented by a JSON string"""
    return json.loads(my_str)
