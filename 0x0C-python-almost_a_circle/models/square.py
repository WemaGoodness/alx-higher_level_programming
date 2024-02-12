#!/usr/bin/python3
"""
This module contains the Square class.

>>> s1 = Square(5)
>>> s1.width
5
>>> s1.height
5
>>> s1.x
0
>>> s1.y
0
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is the Square class. It inherits from the Rectangle class and represents a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This is the constructor of the Square class.

        Args:
            size (int): The size of the Square instance.
            x (int): The x coordinate of the Square instance.
            y (int): The y coordinate of the Square instance.
            id (int): The id of the Square instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size of the Square instance.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size of the Square instance.

        Args:
            value (int): The new size of the Square instance.
        """
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """
        This method assigns attributes.

        Args:
            *args: Non-keyworded arguments.
            **kwargs: Keyworded arguments.
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        This method returns the dictionary representation of a Square.

        Returns:
            dict: The dictionary representation of a Square.
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}


if __name__ == "__main__":
    import doctest
    doctest.testmod()
