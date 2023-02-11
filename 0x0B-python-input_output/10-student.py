#!/usr/bin/python3
""" defines a class student"""


class Student:
    """ defines a class student."""

    def __init__(self, first_name, last_name, age):
        """initialises instance attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance."""
        obj = self.__dict__.copy()

        if type(attrs) is not list:
            return obj
        if not all(isinstance(x, str) for x in attrs):
            return obj
        else:
            new_dict = {}

        for i in range(len(attrs)):
            for key in obj:
                if attrs[i] == key:
                    new_dict[key] = obj[key]
        return new_dict
