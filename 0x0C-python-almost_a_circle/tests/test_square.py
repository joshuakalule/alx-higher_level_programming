#!/usr/bin/python3
"""Test module for the Square class."""
import unittest
from models.square import Square as Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Test class for Square."""
    def setUp(self):
        Base.reset()

    def test_parameters(self):
        with self.assertRaises(TypeError) as cm:
            s = Square(1, "2")
        self.assertEqual(str(cm.exception), "x must be an integer")
   
        with self.assertRaises(TypeError) as cm:
            s = Square(1, 2, "3")
        self.assertEqual(str(cm.exception), "y must be an integer")

        with self.assertRaises(ValueError) as cm:
            s = Square(0)
        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(ValueError) as cm:
            s = Square(1, -2)
        self.assertEqual(str(cm.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as cm:
            s = Square(1, 2, -3)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 89)
        d = {'id': 89, 'size': 10, 'x': 2, 'y': 1}
        s_d = s.to_dictionary()
        self.assertIs(type(s_d), dict)
        self.assertEqual(s_d, d)

    def test_update(self):
        s = Square(3)
        s.update(10)
        self.assertEqual(s.id, 10)
        s.update(10, 4, 2, 3)
        self.assertEqual(s.width, 4)
        self.assertEqual(s.height, 4)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

        s = Square(4, id=89)
        s.update(100, size=10)
        self.assertEqual(s.__str__(), "[Square] (100) 0/0 - 4")

        with self.assertRaises(TypeError):
            s.update(x='string')

        with self.assertRaises(ValueError):
            s.update(size=-80)

    def test__str__(self):
        s = Square(5)
        self.assertEqual(s.__str__(), "[Square] (1) 0/0 - 5")
        s = Square(3, 1, 3)
        self.assertEqual(s.__str__(), "[Square] (2) 1/3 - 3")

        with self.assertRaises(TypeError) as cm:
            s = Square('size')
        self.assertEqual(str(cm.exception), "width must be an integer")

        with self.assertRaises(ValueError) as cm:
            s = Square(-3)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_size_methods(self):
        s = Square(3)
        s.size = 5
        self.assertEqual(s.__str__(), "[Square] (1) 0/0 - 5")
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.size, 5)

        with self.assertRaises(TypeError):
            s.size = 'string'

        with self.assertRaises(ValueError):
            s.size = -98
