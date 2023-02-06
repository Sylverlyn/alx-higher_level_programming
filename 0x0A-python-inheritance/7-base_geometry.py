#!/usr/bin/python3
"""This module creates an empty class."""


class BaseGeometry():
    """Nothing is passed."""

    def area(self):
        """defines the area fundtion.""" 	    
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ function that validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
