#!/usr/bin/python3
"""
This is a unittest for the function max_integer in the module.
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    This class contains unittests for the function max_integer.
    """

    def test_max_integer(self):
        """
        This function tests the max_integer function.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 2, -3, -4]), 2)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)

    def test_max_integer_errors(self):
        """
        This function tests the max_integer function for errors.
        """
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4])
