#!/usr/bin/python3

"""
Module Documentation:
This module defines Rectangle class, represents rectangles & provides various
methods to manipulate them.
"""


class Rectangle:
    """
    Class Documentation:
    Represents rectangles provides methods to calculate area, perimeter,
    and perform comparisons between rectangles.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Constructor Documentation:
        Initializes newinstanceofRectangle class with specified width & height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter Documentation:
        Retrieves the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter Documentation:
        Sets the width of the rectangle with the specified value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter Documentation:
        Retrieves the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter Documentation:
        Sets the height of the rectangle with the specified value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Method Documentation:
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Method Documentation:
        Calculates and returns the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Method Documentation:
        Returns a string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return (str(self.print_symbol) * self.__width + '\n') * self.__height

    def __repr__(self):
        """
        Method Documentation:
        Returns string representation of the rectangle for debugging purposes.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Method Documentation:
        Destructor method prints message when rectangle instance is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static Method Documentation:
        Compares two rectangles and returns one with larger area or equal area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """
        Class Method Documentation:
        Creates a square rectangle with the specified size.
        """
        return cls(size, size)
