#!/usr/bin/python3
"""Module for Base class."""


import json
import csv
import turtle


class Base:
    """Base class.

    Attributes:
        __nb_objects (int): The number of Base objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance.

        Args:
            id (int, optional): The id of the Base object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                list_dicts = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize in CSV."""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary().values())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize from CSV."""
        filename = cls.__name__ + ".csv"
        list_dicts = []
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    list_dicts.append(cls.create(**{k: int(v) for k, v in zip(cls.to_dictionary().keys(), row)}))
        except FileNotFoundError:
            return []
        return list_dicts

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw all the Rectangles and Squares."""
        window = turtle.Screen()
        window.bgcolor("white")
        turtle_obj = turtle.Turtle()

        for rectangle in list_rectangles:
            turtle_obj.penup()
            turtle_obj.goto(rectangle.x, rectangle.y)
            turtle_obj.pendown()
            for _ in range(2):
                turtle_obj.forward(rectangle.width)
                turtle_obj.right(90)
                turtle_obj.forward(rectangle.height)
                turtle_obj.right(90)

        for square in list_squares:
            turtle_obj.penup()
            turtle_obj.goto(square.x, square.y)
            turtle_obj.pendown()
            for _ in range(4):
                turtle_obj.forward(square.size)
                turtle_obj.right(90)

        window.exitonclick()
