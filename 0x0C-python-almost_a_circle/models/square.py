#!/usr/bin/python3
""" square class based on rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ a sqare class that inherits from rectangle class"""
    __size = 0

    def __init__(self, size, x=0, y=0, id=None):
        """initialize sqare class"""

        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """the string representation as [Square] (<id>) <x>/<y> - <size>"""

        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    @property
    def size(self):
        """get/set the size attribute"""
        return self.__size

    @size.setter
    def size(self, size):
        self._validateattr(size, "width")
        self.__size = size
        self.__height = size
        self.__width = size

    def update(self, *args, **kwargs):
        """ update/set arguments of the class.
        if *args is provided: all at ones or any in order of
        id, width, height, x, y
        otherwise if **kwargs is provided set the attributes of the class
        base on key word and value of **kwargs"""

        if args and len(args) > 0:
            if len(args) > 5:
                raise KeyError("no more than 5 keys are allowed")
            map1 = ["id", "size", 'x', 'y']
            for i in range(len(args)):
                if i == 1:
                    self.size = args[i]
                else:
                    self[map1[i]] = args[i]
        else:
            for key, val in kwargs.items():
                if key == "size":
                    self.size = val
                else:
                    self[key] = val

    def to_dictionary(self):
        tmp = {
                "id": self.id,
                "size": self.__size,
                "x": self.x,
                "y": self.y
                }
        return tmp
