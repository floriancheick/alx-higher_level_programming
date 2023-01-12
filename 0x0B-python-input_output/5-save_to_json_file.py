#!/usr/bin/python3
"""
Module 5-save_to_json_file.py
"""


def save_to_json_file(my_obj, filename):
    """writes an Obj to a text file, using a JSON representation"""

    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
