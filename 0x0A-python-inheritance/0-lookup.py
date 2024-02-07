#!/usr/bin/python3
def lookup(obj):
    """
    Function that returns list of available attributes & methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of the names of available attributes and methods of the object.
    """
    return dir(obj)
