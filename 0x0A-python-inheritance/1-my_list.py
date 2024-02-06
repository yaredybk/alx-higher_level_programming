#!/usr/bin/python3
""" class that inherits from list """


def MyList(list):
    """ list class with a print_sorted method"""

    def __init__(self):
        super().__init__()

    """ print the list in asce order"""

    def print_sorted(self):
        print(self.sort())
