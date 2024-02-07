#!/usr/bin/python3
class BaseGeometry:
    """
    A class named BaseGeometry with a method that raises an Exception.
    """

    def area(self):
        """
        Public instance method that raises an Exception with a message.
        """
        raise Exception("area() is not implemented")
