#!/usr/bin/python3
"""
define a square class
"""


class Square:
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """
        initialize square
        args:
            size (int): size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.validate_position(position)
        self.__position = position

    def validate_position(x, y):
        """validates a tuple data for the posion attribute"""
        if type(x) is not int or type(y) is not int or x < 0 or y < 0:
            raise TypeError(
                    "position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """returns the zise attribute"""
        return (self.__size)

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """returns the zise attribute"""
        return (self.__position)

    @position.setter
    def position(self, position=(None, None)):
        self.validate_position(position)
        self.__position = position

    def area(self):
        """returns the current square are"""
        return (self.__size**2)

    def my_print(self):
        """prints a string representation"""
        tmp_s = ""
        for i in range(self.__size):
            for j in range(self.__size):
                tmp_s += "#"
            tmp_s += "\n"
        print(tmp_s[:-1])
