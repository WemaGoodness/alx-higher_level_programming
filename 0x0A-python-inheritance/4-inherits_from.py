#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Function that checks if an object is an instance of a class
    that inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
