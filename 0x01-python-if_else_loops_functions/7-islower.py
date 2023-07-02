#!/usr/bin/python3
# checks for lowercase character.
def islower(c):
    if ord(c) in (97, 123):
        return True
    else:
        return False
