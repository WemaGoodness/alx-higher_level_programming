#!/usr/bin/python3
class BaseGeometry:
    """
    A class named BaseGeometry with methods that
    raise an Exception and validate an integer.

    Methods:
        area: Raises an Exception with a message.
        integer_validator: Validates that a value is a positive integer.
    """

    def area(self):
        """
        Public instance method that raises an Exception with a message.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates that a value is a positive
        integer.

        Args:
            name: The name of the value, assumed to be a string.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
