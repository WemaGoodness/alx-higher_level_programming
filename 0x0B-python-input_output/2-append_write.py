#!/usr/bin/python3
"""
This module contains a function that appends a string at the
end of a text file (UTF8) and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Function to append a string at the end of a text file (UTF8)
    and return the number of characters added.

    Args:
        filename (str): The name of the file to be appended to. Defaults to "".
        text (str): The text to be appended to the file. Defaults to "".

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
