#!/usr/bin/python3
"""
This script adds all command-line arguments to a
Python list and saves them to a file in JSON format.
"""


import sys
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized and saved.
        filename (str): The name of the file to be written to.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f, ensure_ascii=False)


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


def main():
    try:
        existing_data = load_from_json_file('add_item.json')
    except FileNotFoundError:
        existing_data = []

    new_items = sys.argv[1:]
    existing_data.extend(new_items)

    save_to_json_file(existing_data, 'add_item.json')


if __name__ == "__main__":
    main()
