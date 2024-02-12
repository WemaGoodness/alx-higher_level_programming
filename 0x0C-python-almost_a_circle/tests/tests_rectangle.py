#!/usr/bin/python3
"""
This module contains the test cases for the Rectangle class.
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    This is the TestRectangle class.
    """

    def test_area(self):
        """
        This method tests the area method of the Rectangle class.
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)
 

if __name__ == "__main__":
    unittest.main()
