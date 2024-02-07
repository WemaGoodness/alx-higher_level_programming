#!/usr/bin/python3
"""
This module contains a function that converts an object to a
dictionary suitable for JSON serialization.
"""


def class_to_json(obj):
    """
    Converts an object to a dictionary representation for JSON serialization.

    Args:
        obj: The object (instance of a class) to be converted.

    Returns:
        dict: A dictionary containing erializable attributes of the object.
    """
    serializable_attributes = {}
    for attr_name in dir(obj):
        attr_value = getattr(obj, attr_name)
        if isinstance(attr_value, (list, dict, str, int, bool)):
            serializable_attributes[attr_name] = attr_value
    return serializable_attributes
