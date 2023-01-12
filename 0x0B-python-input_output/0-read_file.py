#!/usr/bin/python3
"""This module define a text file-reading function."""


def read_file(filename=""):
    """Print the contents"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
