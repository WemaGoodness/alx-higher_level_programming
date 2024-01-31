#!/usr/bin/python3
class LockedClass:
    """A class that prevents creation of new instance attributes"""
    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        """Initialize the instance attribute first_name"""
        self.first_name = first_name
