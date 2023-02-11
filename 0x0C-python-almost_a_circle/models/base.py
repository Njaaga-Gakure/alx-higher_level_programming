#!/usr/bin/python3
"""class Base module."""


import json


class Base:
    """Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Assign id to instance.

        args:
            id (int): instance id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        args:
            list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        args:
            list_objs: a list of instances who inherits from Base
        """
        filename = cls.__name__ + ".json"
        dict_list = []
        with open(filename, 'w', encoding="utf-8") as f:
            if list_objs:
                for o in list_objs:
                    dict_list.append(o.to_dictionary())
            f.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Return a list represented by a JSON string.

        args:
            json_string: the JSON string
        """
        if json_string is None:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set.

        args:
            dictionary: attributes of the instance
        """
        if dictionary and len(dictionary) != 0:
            if cls == "Rectangle":
                obj = cls(6, 7, 8)
            else:
                obj = cls(5, 7, 9)
            obj.update(**dictionary)
            return (obj)

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances.

        args:
            cls: a class
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                dict_list = cls.from_json_string(f.read())
                return [cls.create(**dictionary) for dictionary in dict_list]
        except FileNotFoundError:
            return ([])
