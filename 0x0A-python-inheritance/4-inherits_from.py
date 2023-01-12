#!/usr/bin/python3
"""This module define an inherited class-chekcing function."""


def inherits_from(obj, a_class):
    """"This check if an object  is an inherited instance of a class."""
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
