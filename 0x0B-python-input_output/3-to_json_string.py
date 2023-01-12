#!/usr/bin/python3
"""
Module 3-to_json_string.py
"""


def to_json_string(my_obj):
    """returns the JSON representation of an obj (string)"""
    import json

    return json.dumps(my_obj)
