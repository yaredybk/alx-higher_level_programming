#!/usr/bin/python3
"""
Rectangle classs that inherits from base class that hase id attribute
"""
from models.base import Base


class Rectangle(Base):
    """
    rectangle class with width, height, x, y and id attributes
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        inializes the rectangle class with a private checker class

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
        """
	get/set the width attribute
	"""
        return self.__width

    @width.setter
    def width(self, width):
        """
	set the width
	"""
        self._validate_set(width, "width")

    @property
    def height(self):
        """
	get/set the height attribute
	"""
        return self.__height

    @height.setter
    def height(self, height):
        """
	set height
	"""
        self._validate_set(height, "height")

    @property
    def x(self):
        """
	get/set the x attribute
	"""
        return self.__x

    @x.setter
    def x(self, x):
        """
	set attribute x
	"""
        self._validate_set(x, 'x')

    @property
    def y(self):
        """
	get/set the y attribute
	"""
        return self.__y

    @y.setter
    def y(self, y):
        """
	set attribute y
	"""
        self._validate_set(y, 'y')

    def _validateattr(self, val, key="input"):
        """
	validates if val is an int and above 0 and
        sets an atribute <key> to <val> otherwise raises an error
	"""

        if type(val) is not int:
            raise TypeError(f"{key} must be an integer")
        elif key == 'x' or key == 'y':
            if val < 0:
                raise ValueError(f"{key} must be >= 0")
        elif val <= 0:
            raise ValueError(f"{key} must be > 0")

    def _validate_set(self, val, key):
        """
	validates value and set an attribute
	"""
        self._validateattr(val, key)
        self[key] = val
