#!/usr/bin/python3
"""
This module contains a function that prints a square with the character #.
"""


def print_square(size):
    """
    This function takes one parameter: size.
    It prints a square of size 'size' with the character #.
    Size should be an integer and greater than or equal to 0.
    If size is not an integer or less than 0, a TypeError or ValueError is raised.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
