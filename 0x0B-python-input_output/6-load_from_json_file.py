#!/usr/bin/python3
"""
This module contains a function that creates an object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to be loaded.

    Returns:
        object: The Python data structure represented by the JSON content.
    """
    with open(filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)
