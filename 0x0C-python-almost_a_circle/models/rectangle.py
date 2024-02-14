#!/usr/bin/python3
"""Rectangle classs that inherits from base class that hase id attribute"""
from models.base import Base


class Rectangle(Base):
    """rectangle class with width and height"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """inializes the rectangle class with a private checker class

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self._validate_set(width, "width")
        self._validate_set(height, "height")
        self._validate_set(x, 'x')
        self._validate_set(y, 'y')
        super().__init__(id)

    @property
    def width(self):
        """get/set the width attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """set the width"""
        self._validate_set(width, "width")

    @property
    def height(self):
        """get/set the height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """set height"""
        self._validate_set(height, "height")

    @property
    def x(self):
        """get/set the x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """set attribute x"""
        self._validate_set(x, 'x')

    @property
    def y(self):
        """get/set the y attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """set attribute y"""
        self._validate_set(y, 'y')

    def _validateattr(self, val, key="input"):
        """validates if val is an int and above 0 and
        sets an atribute <key> to <val> otherwise raises an error"""

        if type(val) is not int:
            raise TypeError(f"{key} must be an integer")
        elif key == 'x' or key == 'y':
            if val < 0:
                raise ValueError(f"{key} must be >= 0")
        elif val <= 0:
            raise ValueError(f"{key} must be > 0")

    def _validate_set(self, val, key):
        """validates value and set an attribute"""
        self._validateattr(val, key)
        self[key] = val

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        str1 = '\n' * self.__y
        str2 = ' ' * self.__x + '#' * self.__width
        str1 += '\n'.join([str2 for _ in range(self.__height)])
        print(str1)

    def __str__(self):
        """returns str representation in a format like:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}")

    def __setitem__(self, key, value):
        if (key == "id"):
            self.id = value
        elif (key == "width"):
            self.__width = value
        elif (key == "height"):
            self.__height = value
        elif (key == 'x'):
            self.__x = value
        elif (key == 'y'):
            self.__y = value
        else:
            raise KeyError(f"'{key}' id invalid key")

    def update(self, *args, **kwargs):
        """ update/set arguments of the class.
        if *args is provided: all at ones or any in order of
        id, width, height, x, y
        otherwise if **kwargs is provided set the attributes of the class
        base on key word and value of **kwargs"""

        if args and len(args) > 0:
            if len(args) > 5:
                raise KeyError("no more than 5 keys are allowed")
            map1 = ["id", "width", "height", 'x', 'y']
            for i in range(len(args)):
                self[map1[i]] = args[i]
        else:
            for key, val in kwargs.items():
                self[key] = val

    def to_dictionary(self):
        tmp = {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }
        return tmp
