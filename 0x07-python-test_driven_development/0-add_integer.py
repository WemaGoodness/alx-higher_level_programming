#!/usr/bin/python3
"""
This module contains a function add_integer that adds two integers.

The function takes two parameters: a & b. Both a & b must be integers/floats.
If either a or b is a float, it is casted to an integer before addition.
If either a or b is not an integer or float, a TypeError exception is raised.
The function returns the sum of a and b.
"""


def add_integer(a, b=98):
    """
    Function to add two integers.

    Parameters:
    a (int, float): The first number to add.
    b (int, float): The second number to add. Default is 98.

    Returns:
    int: The sum of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
