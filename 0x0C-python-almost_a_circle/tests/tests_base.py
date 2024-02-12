#!/usr/bin/python3
"""
This module contains the TestBase class.
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    This is the TestBase class.
    """

    def setUp(self):
        """
        This method sets up the test environment.
        """
        Base.__nb_objects = 0

    def test_id(self):
        """
        This method tests the id attribute of the Base class.
        """
        base1 = Base()
        self.assertEqual(base1.id, 1)

        base2 = Base()
        self.assertEqual(base2.id, 2)

        base3 = Base(12)
        self.assertEqual(base3.id, 12)

        base4 = Base()
        self.assertEqual(base4.id, 3)


if __name__ == "__main__":
    unittest.main()
