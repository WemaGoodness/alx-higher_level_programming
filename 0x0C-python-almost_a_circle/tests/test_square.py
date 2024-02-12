#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_size(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_update_args(self):
        s1 = Square(5)
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

    def test_update_kwargs(self):
        s1 = Square(5)
        s1.update(size=7, x=8, y=9, id=10)
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.x, 8)
        self.assertEqual(s1.y, 9)

    def test_to_dictionary(self):
        s1 = Square(5, 1, 2, 3)
        s1_dict = s1.to_dictionary()
        expected_dict = {"id": 3, "size": 5, "x": 1, "y": 2}
        self.assertEqual(s1_dict, expected_dict)


if __name__ == "__main__":
    unittest.main()
