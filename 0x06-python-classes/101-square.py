class Square:
    """
    This class defines a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the Square.
        """
        self.size = size
        self.position = position

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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the Square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the Square.
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Return the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the Square with the character #.
        """
        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    def __str__(self):
        """
        Return a string representation of the Square.
        """
        if self.__size == 0:
            return ""
        result = "\n" * self.__position[1]
        for _ in range(self.__size):
            result += " " * self.__position[0]
            result += "#" * self.__size
            result += "\n"
        return result[:-1]
