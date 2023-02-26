#!/usr/bin/python3
"""module defines a class Base"""
import json


class Base:
    """defines a class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialises a method"""
        if id is not None:
            self.id = id
        else:
             Base.__nb_objects += 1
             self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string representative of an object."""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string representation of list_objs to a file."""
        if list_objs is None:
            return []
        else:
            if all(isinstance(obj, Base) for obj in list_objs) or issubclass(cls.__name__, Base):
                dict_list = [obj.to_dictionary() for obj in list_objs]
                file = cls.to_json_string(dict_list)

        with open(f"{cls.__name__}.json", 'w') as f:
            f.write(file)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return (json.loads(json_string))
        
    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            newclass = cls(1, 1)
        elif cls.__name__ == "Square":
            newclass = cls(1)
        else:
            newclass = None
        newclass.update(**dictionary)
        return newclass
    
