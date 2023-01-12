#!/usr/bin/python3
"""
Module 6-load_from_json_file.py
"""


def load_from_json_file(filename):
    """“JSON file”"""

    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
