#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """A class representING a square with PrIA size & position"""

    def __init__(self, size=0, position=(0, 0)):
        """This method initializes the square with a given size & position"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """This method retrieves the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """This method sets the position"""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(n, int) for n in value) or \
           not all(n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This method returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """This method prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            lines = [
                    " " * self.__position[0] + "#" * self.__size
                    for _ in range(self.__size)
                    ]
            print("\n".join(lines))
