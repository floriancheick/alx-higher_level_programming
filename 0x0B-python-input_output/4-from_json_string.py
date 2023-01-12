#!/usr/bin/python3
"""
Module 4-from_json_string.py
"""


def from_json_string(my_str):
    """returns python data structure frm JSON"""
    import json

    return json.loads(my_str)
