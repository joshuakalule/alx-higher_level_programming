#!/usr/bin/python3
""" 5. Max integer - Unittest """
import unittest
m = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ class to test the method max_integer """

    def test_max_integer(self):
        """ method to test if the function returns the max integer """
        # normal 1
        self.assertEqual(m([1, 2, 0]), 2)

        # normal 2
        self.assertEqual(m([-4, -3, -1]), -1)

        # missing argument
        self.assertIsNone(m())
        self.assertIsNone(m([]))

        # list with one element
        self.assertEqual(m([45]), 45)

        # list with the max at the beginning
        self.assertEqual(m([10, 1, 2, 3]), 10)
