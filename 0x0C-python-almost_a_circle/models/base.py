#!/usr/bin/python3
"""
Module: Base
base.by - other classes may inherit from this Base class
"""
import json


class Base:
    """ Class: Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string repr. of object """
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string repr. of object """
        new_list = []
        filename = "{}.json".format(cls.__name__)

        if list_objs is None:
            return new_list
        else:
            with open(filename, "w", encoding="UTF8") as my_json:
                for objects in list_objs:
                    new_list.append(cls.to_dictionary(objects))
                my_json.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ returns list of JSON string repr. of object """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns instance with all attributes of object set """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ is "Rectangle":
            dummy = Rectangle(1, 1)
        if cls.__name__ is "Square":
            dummy = Square(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns list of instances """
        new_list = []
        filename = "{}.json".format(cls.__name__)

        try:
            with open(filename, "r", encoding="UTF8") as my_json:
                for instance in cls.from_json_string(my_json.read()):
                    new_list.append(cls.create(**instance))
                return new_list
        except:
            return []
