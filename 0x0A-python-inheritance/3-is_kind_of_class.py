#!/usr/bin/python3
"""
This module define a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """This check if an object is an instance or inherited instance
of class."""
    return isinstance(obj, a_class)
