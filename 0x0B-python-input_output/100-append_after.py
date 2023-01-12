#!/usr/bin/python3
"""
Module 100-append_after.py
"""


def append_after(filename="", search_string="", new_string=""):
    """append new_strings"""

    with open(filename, mode="r+", encoding="utf-8") as f:
        data = ""
        for line in f:
            data += line
            if search_string in line:
                data += new_string
        f.seek(0)
        f.write(data)
