#!/usr/bin/python3
"""
Module 12-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
"""

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    le = [[1]]
    for row in range(n-1):
        le.append([i+j for i, j in
                   zip([0]+le[-1], le[-1] + [0])])
    return le
