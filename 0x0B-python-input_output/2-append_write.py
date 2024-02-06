#!/usr/bin/python3
"""defines a function that appends text to a file"""


def append_write(filename="", text=""):
    """append a text to a file"""

    with open(filename, mode="a", encoding="utf-8") as file2:
        return file2.write(text)
