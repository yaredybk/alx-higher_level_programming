#!/usr/bin/python3
""" “base” of all other classes in this project"""
import json


class Base:
    """ “base” of all other classes in this project
    manage id attribute in all your future classes and
    to avoid duplicating the same code (by extension, same bugs)"""

    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        try:
            for ele in list_objs:
                name = ele.__class__.__name__
                print(f"name: {name}")
                tmpstr = ele.to_json_string(ele.to_dictionary())
                with open(f"{name}.json", "w", encoding="utf8") as file:
                    file.write(tmpstr)
        except IOError as e:
            raise IOError(f"Error writing to file: {e}")

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""

        if json_string is None:
            return ([])
        return (json.loads(json_string))
