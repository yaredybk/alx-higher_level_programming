#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """return the dictionary repr of a simple data"""
    return obj.__dict__
