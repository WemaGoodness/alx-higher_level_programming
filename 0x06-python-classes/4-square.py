#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """This class represents a square with a private instance attribute size"""

    def __init__(self, size=0):
        """This method initializes the square with a given size"""
        self.size = size

    @property
    def size(self):
        """This method retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """This method sets the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """This method returns the current square area"""
        return self.__size ** 2
