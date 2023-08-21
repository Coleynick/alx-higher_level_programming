#!/usr/bin/python3
""" Base """


import json


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save json to file """
        filename = cls.__name__ + ".json"
        obj_lisst = []

        if list_objs is not None:
            for obj in list_objs:
                obj_lisst.append(obj.to_dictionary())

        with open(filename, mode='w', encoding='utf-8') as ifile:
            ifile.write(cls.to_json_string(obj_lisst))

    def from_json_string(json_string):
        """
        Converts JSON to a lisst of dicts.

        Args:
            json_string (str): JSON (str) rep of a list.

        Returns:
            list: (of dictionaries).
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance using a dict of attr.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads inst from JSON ifile."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as ifile:
                dataa = ifile.read()
                if dataa:
                    lisst_dicts = cls.from_json_string(dataa)
                    inst = [cls.create(**dic) for dic in lisst_dicts]
                    return inst
                else:
                    return []
        except FileNotFoundError:
            return []
