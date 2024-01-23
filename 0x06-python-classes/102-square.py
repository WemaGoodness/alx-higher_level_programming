#!/usr/bin/python3
"""This module defines a square"""


class Square:
    """
    This class defines a square.
    """

    def __init__(self, size=0):
        """
        Initialize the Square.
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the Square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the Square.
        """
        if type(value) not in [int, float]:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return the current square area.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Check if two Squares are equal.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Check if two Squares are not equal.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Check if a Square is less than another one.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Check if a Square is less than or equal to another one.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

    def __gt__(self, other):
        """
        Check if a Square is greater than another one.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Check if a Square is greater than or equal to another one.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False
