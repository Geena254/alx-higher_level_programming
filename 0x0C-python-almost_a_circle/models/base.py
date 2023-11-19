#!/usr/bin/python3
"""This module is for the first Base Class Model"""
import json
import csv


class Base():
    """This is the base class model
    with a counter for handeling ids

        Attributes:
            __nb_objects = counter for the ids
    """
    __nb_objects = 0

    # Built in Functions
    def __init__(self, id=None):
        """Initialization of Base Object
            Arguments:
                id: id for the object, if id is None then assign __nb_objects
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # Static methods

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None:
            return "[]"
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None:
            return ([])
        if type(json_string) is not str:
            raise TypeError("json_string must be a string")
        return json.loads(json_string)

    # Class methods

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        with open(f"{cls.__name__}.json", 'w+') as f:
            obj_list = []
            if list_objs is None:
                f.write(cls.to_json_string(obj_list))
            else:
                for item in list_objs:
                    obj_list.append(cls.to_dictionary(item))
                f.write(cls.to_json_string(obj_list))
