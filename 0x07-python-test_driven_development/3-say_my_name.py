#!/usr/bin/python3
"""
This module contains a function say_my_name that prints
"My name is <first name> <last name>".
"""

def say_my_name(first_name, last_name=""):
    """
    This function takes two parameters: first_name and last_name.
    It prints "My name is <first name> <last name>".
    Both first_name and last_name should be strings.
    If either is not a string, a TypeError is raised.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
