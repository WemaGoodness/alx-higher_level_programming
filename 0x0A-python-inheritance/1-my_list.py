#!/usr/bin/python3
class MyList(list):
    """
    A class that inherits from list and has a method to print the list sorted.

    Methods:
        print_sorted: Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
