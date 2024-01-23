#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """This class represents a square with a private instance attribute size"""

    def __init__(self, size=0):
        """This method initializes the square with a given size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """This method returns the current square area"""
        return self.__size ** 2
