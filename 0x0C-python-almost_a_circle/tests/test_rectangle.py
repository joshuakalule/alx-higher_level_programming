#!/usr/bin/python3
""" Test module for Rectangle class """
import unittest
from models.rectangle import Rectangle as R
from models.base import Base
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):
    """ test the Rectangle class """

    def setUp(self):
        Base.reset()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output = StringIO()

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_to_dictionary(self):
        r = R(1, 2, 3, 4, 89)
        self.assertIs(type(r.to_dictionary()), dict)
        d = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4} 
        self.assertEqual(r.to_dictionary(), d)

    
    def test_update(self):
        r = R(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        
        with self.assertRaises(ValueError) as cm:
            r.update(89, 2, 3, 4, -5)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_update_2(self):
        r = R(10, 10, 10, 10)
        r.update(width=2)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 10/10 - 2/10")
        r.update(x=4, height=3, y=5, id=89)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        r.update(100, 99, x=-8, y=-9)
        self.assertEqual(r.__str__(), "[Rectangle] (100) 4/5 - 99/3")
        
        with self.assertRaises(ValueError) as cm:
            r.update(y=-5)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test__str_(self):
        r = R(4, 6, 2, 1, 12)
        self.assertEqual(r.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r = R(5, 5, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 1/0 - 5/5")

    def test_attributes(self):
        r1 = R(2, 3)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r3 = R(1, 1, 1, 1, 89)
        self.assertEqual(r3.id, 89)

        r2 = R(5, 3, 1, 2)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)

        with self.assertRaises(TypeError):
            r4 = R()

        regex = r"^(width|height|x|y) must be an integer"
        with self.assertRaises(TypeError) as cm:
            r4 = R('one', 2, 3, 4)
        self.assertRegex(str(cm.exception), regex)
        
        with self.assertRaises(TypeError) as cm:
            r4 = R(1, 'two', 3, 4)
        self.assertRegex(str(cm.exception), regex)
        
        with self.assertRaises(TypeError) as cm:
            r4 = R(1, 2, 'three', 4)
        self.assertRegex(str(cm.exception), regex)

        with self.assertRaises(TypeError) as cm:
            r4 = R(1, 2, 3, 'four')
        self.assertRegex(str(cm.exception), regex)

        
        regex = r"^(width|height|x|y) must be (>|>=) 0"
        with self.assertRaises(ValueError) as cm:
            r4 = R(-1, 2, 3, 4)
        self.assertRegex(str(cm.exception), regex)

        with self.assertRaises(ValueError) as cm:
            r4 = R(1, -2, 3, 4)
        self.assertRegex(str(cm.exception), regex)
        
        with self.assertRaises(ValueError) as cm:
            r4 = R(0, 2, 3, 4)
        self.assertRegex(str(cm.exception), regex)

        with self.assertRaises(ValueError) as cm:
            r4 = R(1, 0, 3, 4)
        self.assertRegex(str(cm.exception), regex)

        with self.assertRaises(ValueError) as cm:
            r4 = R(1, 2, -3, 4)
        self.assertRegex(str(cm.exception), regex)

        with self.assertRaises(ValueError) as cm:
            r4 = R(1, 2, 3, -4)
        self.assertRegex(str(cm.exception), regex)
    
    def test_area(self):
        r = R(4, 3)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        r = R(4, 3)
        r.display()
        expected_output = "####\n####\n####\n"
        self.assertEqual(self.output.getvalue(), expected_output, msg="Rectangles do not match")
    
    def test_display_2(self):
        r = R(2, 3, 2, 2)
        r.display()
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(self.output.getvalue(), expected_output, msg="Rectangles do not match")


if __name__ == "__main__":
    unittest.main()
