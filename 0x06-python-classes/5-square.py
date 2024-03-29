#!/usr/bin/python3
"""
define a square class
"""


class Square:
    """square class"""

    def __init__(self, size=0):
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
