#!/usr/bin/python3
"""1. Base class."""
import json
import os
import turtle


class Base:
    """Base class for shapes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Define the shape parameters."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize from csv."""
        shape = cls.__name__
        ref = {
            'Square': ['id', 'size', 'x', 'y'],
            'Rectangle': ['id', 'width', 'height', 'x', 'y']
        }
        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return []
        ret_list = list()
        with open(filename, 'r') as f:
            for line in f:
                line = line.replace('\n', '')
                line_iter = iter(line.split(','))
                obj_dict = dict()
                for attr in ref[shape]:
                    obj_dict[attr] = int(next(line_iter))
                ret_list.append(cls.create(**obj_dict))
        return ret_list

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            list_dict = Base.from_json_string(f.read())
        ret_list = list()
        for d in list_dict:
            ret_list.append(cls.create(**d))
        return ret_list

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set."""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 2)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            return None
        if len(dictionary) == 0:
            return None
        dummy.update(**dictionary)
        return dummy

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation."""
        if json_string is None or len(json_string) == 0:
            return list()
        return json.loads(json_string)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize in CSV."""
        filename = f"{cls.__name__}.csv"
        shape = cls.__name__
        ref = {
            'Square': ['id', 'size', 'x', 'y'],
            'Rectangle': ['id', 'width', 'height', 'x', 'y']
        }
        if list_objs is None or len(list_objs) == 0:
            string = ",,,," if shape == "Rectangle" else ",,,"
        else:
            string = str()
            for obj in list_objs:
                list_attrs = list()
                for attr in ref[shape]:
                    list_attrs.append(str(getattr(obj, attr, '')))
                string += ",".join(list_attrs)+'\n'

        with open(filename, 'w') as f:
            f.write(string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to a file."""
        filename = f"{cls.__name__}.json"
        if list_objs is None or len(list_objs) == 0:
            string = Base.to_json_string([])
        else:
            list_dict = list()
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
            string = Base.to_json_string(list_dict)

        with open(filename, 'w') as f:
            f.write(string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def reset(cls):
        """Set instance count back to 0."""
        Base.__nb_objects = 0

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw shapes in a GUI."""
        window = turtle.Screen()
        window.bgcolor("white")

        pen = turtle.Turtle()
        pen.speed(1)

        for rectangle in rectangle_list:
            width = rectangle.width
            height = rectangle.height
            x = rectangle.x
            y = rectangle.y
            color = "green"

            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.color(color)
            for _ in range(2):
                pen.forward(width)
                pen.left(90)
                pen.forward(height)
                pen.left(90)

        for square in square_list:
            size = square.size
            x = square.x
            y = square.y
            color = "blue"

            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.color(color)
            for _ in range(4):
                pen.forward(side)
                pen.left(90)

        turtle.done()
