#!/usr/python3
"""define a function that writes in to files"""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file."""

    with open(filename, mode="w", encoding="utf-8") as file1:
        return file1.write(text)
