#!/usr/bin/python3
"""
“base” of all other classes in this project
"""
import json
import turtle


class Base:
    """
    base of all other classes in this project
    manage id attribute in all your future classes and
    to avoid duplicating the same code (by extension, same bugs)
    """

    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set from a dict
        """

        new = cls(1, 1)
        new.update(**dictionary)
        return (new)

    @classmethod
    def create_from_list(cls, *items):
        """
        returns an instance with all attributes already set from a dict
        """

        new = cls(1, 1)
        new.update(*items)
        return (new)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """

        try:
            name = cls.__name__
            tmpstr = [x.to_json_string(x.to_dictionary()) for x in list_objs]
            with open(f"{name}.json", 'w', encoding="utf8") as file:
                file.write('\n'.join(tmpstr))
        except IOError as e:
            raise IOError(f"Error writing to file: {e}")

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances from a file
        """

        try:
            with open(f"{cls.__name__}.json", "r") as f:
                return ([cls.create(**cls.from_json_string(x)) for x in f])
        except FileNotFoundError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a csv file
        """

        try:
            name = cls.__name__
            if name == "Rectangle":
                tmpstr = [f"{x.id},{x.width},{x.height},{x.x},{x.y}"
                          for x in list_objs]
            else:
                tmpstr = [f"{x.id},{x.size},{x.x},{x.y}"
                          for x in list_objs]
            with open(f"{name}.json", 'w', encoding="utf8") as file:
                file.write('\n'.join(tmpstr))
        except IOError as e:
            raise IOError(f"Error writing to file: {e}")

    @classmethod
    def load_from_file_csv(cls):
        """
        returns a list of instances from a csv file
        """

        try:
            with open(f"{cls.__name__}.json", "r") as f:
                return ([cls.create_from_list(*[int(y) for y in x.split(',')])
                        for x in f])
        except FileNotFoundError:
            return ([])

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """

        if list_dictionaries is None:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
         returns the list of the JSON string representation json_string
        """

        if json_string is None:
            return ([])
        return (json.loads(json_string))

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
         draw rectangle or/and square to a canvas
        """

        tt = turtle.Turtle()
        tt.screen.bgcolor(100, 100, 100)
        tt.color((0, 0, 0), (0, 0, 200))
        tt.mode("standard")
        for r in list_rectangles:
            __loop(r)
        tt.color((0, 200, 0), (200, 0, 200))
        for s in list_squares:
            __loop(s)

        @staticmethod
        def __loop(r):
            tt.penup()
            tt.goto(x - (r.width / 2), y + (r.height / 2))
            tt.setheading(0)
            tt.pendown()
            tt.begin_fill()
            tt.forward(r.width)
            tt.setheading(-90)
            tt.forward(r.height)
            tt.setheading(0)
            tt.backward(r.width)
            tt.setheading(90)
            tt.forward(r.height)
            tt.end_fill()
            tt.penup()
