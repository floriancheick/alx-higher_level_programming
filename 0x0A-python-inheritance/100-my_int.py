#!/usr/bin/python3
"""
Module 100-my_int.py
"""


class MyInt(int):
    """
    defines class MyInt and inherits from int
    """

    def __init__(self, fig):
        """Initializes fig"""
        self.fig = fig

    def __eq__(self, other):
        """returns false if both are equal"""
        return self.fig != other

    def __ne__(self, other):
        """returns false if both are not equal"""
        return self.fig == other
