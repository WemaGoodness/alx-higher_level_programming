#!/usr/bin/python3
"""
This module defines a Rectangle class.
The Rectangle class defines a rectangle by its width and height.
"""


class Rectangle:
    """
    Rectangle class with width and height attributes.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize Rectangle instance with optional width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the Rectangle.
        If width is not an integer, raise a TypeError.
        If width is less than 0, raise a ValueError.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the Rectangle.
        If height is not an integer, raise a TypeError.
        If height is less than 0, raise a ValueError.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the Rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the Rectangle.
        If width or height is 0, return 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the Rectangle.
        If width or height is 0, return an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Return string representation of Rectangle used to recreate the object.
        """
        return f"Rectangle({self.__width}, {self.__height})"
