#!/usr/bin/python3
"""
Module 1-write_file.py
"""


def write_file(filename="", text=""):
    """writes a string to text file, returns number of char"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
