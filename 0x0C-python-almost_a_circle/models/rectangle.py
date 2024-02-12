#!/usr/bin/python3
"""
This module contains the Rectangle class.

>>> r1 = Rectangle(10, 2)
>>> r1.width
10
>>> r1.height
2
>>> r1.x
0
>>> r1.y
0
>>> r1.area()
20
"""

from models.base import Base


class Rectangle(Base):
    """
    This is the Rectangle class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This is the constructor of the Rectangle class.

        Args:
            width (int): The width of the Rectangle instance.
            height (int): The height of the Rectangle instance.
            x (int): The x coordinate of the Rectangle instance.
            y (int): The y coordinate of the Rectangle instance.
            id (int): The id of the Rectangle instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        This method returns the area of the Rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """
        This method prints in stdout the Rectangle instance with the character #.
        """
        print('\n' * self.__y, end="")
        print((" " * self.__x + "#" * self.__width + "\n") * self.__height, end="")

    def __str__(self):
        """
        This method returns the string representation of the Rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        This method assigns an argument to each attribute.
        """
        attributes = ["id", "width", "height", "x", "y"]
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        This method returns the dictionary representation of a Rectangle.
        """
        return {'id': self.id, 'width': self.__width, 'height': self.__height, 'x': self.__x, 'y': self.__y}


if __name__ == "__main__":
    import doctest
    doctest.testmod()
