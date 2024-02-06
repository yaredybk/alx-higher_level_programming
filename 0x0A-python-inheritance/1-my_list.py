#!/usr/bin/python3
""" class that inherits from list """


def MyList(list):
    """ list class with a print_sorted method"""

    def __init__(self,list=[]):
        super().__init__(list)

    def print_sorted(self):
        print(sorted(self))
