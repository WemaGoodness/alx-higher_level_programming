#!/usr/bin/python3
class Square(Rectangle):
    """
    A class named Square that inherits from Rectangle.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        The constructor for the Square class.

        Parameters:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Public instance method that returns the area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
