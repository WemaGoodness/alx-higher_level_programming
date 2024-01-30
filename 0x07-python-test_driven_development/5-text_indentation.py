#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new
lines after each of these characters: ., ? and :.
"""


def text_indentation(text):
    """
    This function takes one parameter: text.
    Prints text with 2 new lines after each of these characters: ., ? and :.
    Text should be a string.
    If text is not a string, a TypeError is raised.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    print("\n".join(line.strip() for line in text.split("\n")))
