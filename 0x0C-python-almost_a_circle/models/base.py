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
