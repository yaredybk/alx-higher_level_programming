#!/usr/bin/python3
"""
check if type is either integer or float
"""


def check_num(num):
    if isinstance(num, int):
        return True
    if isinstance(num, float):
        return True
    return False


"""
adds 2 integers
"""


def add_integer(a, b=98):
    if check_num(a) is False:
        raise TypeError("a must be an integer")
    if check_num(b) is False:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
