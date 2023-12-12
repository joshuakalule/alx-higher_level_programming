#!/usr/bin/python3
""" Test module for the Base class """
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle as Rectangle
from models.square import Square as Square
import json
import os


class TestBase(unittest.TestCase):
    """ test the Base class """

    def setUp(self):
        Base.reset()
    
    def test_load_from_file_rectangle(self):
        filename = 'Rectangle.json'
        f_str = '[\
            {"id": 89, "width": 3, "height": 4, "x": 2, "y": 1},\
            {"id": 1, "width": 2, "height": 3, "x": 0, "y": 0}]'
        with open(filename, 'w') as f:
            f.write(f_str)

        list_objs = Rectangle.load_from_file()
        self.assertTrue(type(list_objs), list)

        r1 = list_objs[0]
        self.assertIs(type(r1), Rectangle)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 1)

        r2 = list_objs[1]
        self.assertIs(type(r2), Rectangle)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        if os.path.exists(filename):
            os.remove(filename)
        self.assertEqual(Rectangle.load_from_file(), [])
    
    def test_load_from_file_square(self):
        filename = 'Square.json'
        f_str = '[\
            {"id": 89, "size": 4, "x": 2, "y": 1},\
            {"id": 1, "size": 3, "x": 0, "y": 0}]'
        with open(filename, 'w') as f:
            f.write(f_str)

        list_objs = Square.load_from_file()

        self.assertTrue(type(list_objs), list)

        s1 = list_objs[0]
        self.assertIs(type(s1), Square)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 1)

        s2 = list_objs[1]
        self.assertIs(type(s2), Square)
        self.assertEqual(s2.id, 1)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 0)
        self.assertEqual(s2.y, 0)

        if os.path.exists(filename):
            os.remove(filename)
        self.assertEqual(Square.load_from_file(), [])


    def test_create_rectangle(self):
        d = {'id': 89, 'width': 3, 'height': 4, 'x': 2, 'y': 1}
        r = Rectangle.create(**d)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)

        r2 = Rectangle.create()
        self.assertIsNone(r2)

    def test_create_square(self):
        d = {'id': 100, 'size': 4, 'x': 1, 'y': 0}
        s = Square.create(**d)
        self.assertEqual(s.id, 100)
        self.assertTrue(s.size==s.width==s.height==4)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 0)

        s2 = Square.create()
        self.assertIsNone(s2)

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(98)
        self.assertEqual(b3.id, 98)
        b4 = Base()
        self.assertEqual(b4.id, 3)
        with self.assertRaises(TypeError) as cm:
            b5 = Base(1, 2)

    def test_from_json_string(self):
        json_string = '[{"height": 4, "width": 10, "id": 89},\
        {"height": 7, "width": 1, "id": 7}]'
        list_dict = [
                    {'id': 89, 'width': 10, 'height': 4}, 
                    {'id': 7, 'width': 1, 'height': 7}
                ]

        self.assertEqual(Base.from_json_string(json_string), list_dict)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_save_to_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        d = [
            {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
            {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}
        ]
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json") as f:
            self.assertEqual(json.load(f), d)

        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(json.load(f), [])

        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(len(json.load(f)), 0)

    def test_save_to_file_square(self):
        s1 = Square(10)
        s2 = Square(5, 1, 2, id=89)
        d = [
            {'id': 1, 'size': 10, 'x': 0, 'y': 0},
            {'id': 89, 'size': 5, 'x': 1, 'y': 2}
        ]
        Square.save_to_file([s1, s2])
        with open("Square.json") as f:
            self.assertEqual(json.load(f), d)

        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(json.load(f), [])
        
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(json.load(f), [])

    def test_to_json_string(self):
        list_dict = [
            {'id': 89, 'size': 10, 'x': 2, 'y': 1},
            {'id': 1, 'size': 5, 'x': 0, 'y': 0}
        ]
        json_string = Base.to_json_string(list_dict)

        self.assertIs(type(json_string), str)
        self.assertEqual(json.loads(json_string), list_dict)

if __name__ == "__main__":
    unittest.main()
    Base.reset()
