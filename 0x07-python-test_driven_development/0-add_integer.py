#!/usr/bin/python3
# 0-add_integer.py
""" Defines an integer adddition function."""
def add_integer(a, b=98):
    """Return an integer addition of a and b."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
