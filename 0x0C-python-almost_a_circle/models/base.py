#!/usr/bin/python3
"""
Defines a Base class
"""
import json
import csv
import turtle

class Base:
    """Base class implemenation
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        defines private class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert to string"""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
