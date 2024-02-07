#!/usr/bin/python3
"""
This module defines a Student class.

The Student class has three public instance attributes:
first_name, last_name, and age.
It also has methods to_json() and reload_from_json()
for serialization and deserialization.
"""


class Student:
    """
    Student class that defines a student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Parameters:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute
        names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved.

        Parameters:
        attrs (list): A list of strings representing attribute names.

        Returns:
        dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if attr in self.__dict__}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Parameters:
        json (dict): A dictionary where the key is the public attribute
        name and the value is the value of the public attribute.
        """
        for key, value in json.items():
            setattr(self, key, value)
