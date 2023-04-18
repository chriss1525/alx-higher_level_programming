#!/usr/bin/python3
"""this module defines test cases for square.pyS"""
import io
from models.square import Square
from models.base import Base
import unittest


class TestSquare(unittest.TestCase):
    """tests"""


    def test_init(self):
        Base._Base__nb_objects = 0
        s = Square(5)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

        s = Square(7, 2, 3, 5)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_size_property(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_update(self):
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)
        s.update(10, 8)
        self.assertEqual(s.size, 8)
        s.update(10, 8, 4)
        self.assertEqual(s.x, 4)
        s.update(10, 8, 4, 2)
        self.assertEqual(s.y, 2)
        s.update(id=15)
        self.assertEqual(s.id, 15)
        s.update(size=20)
        self.assertEqual(s.size, 20)
        s.update(x=3, y=5)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 5)

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 10)
        expected_dict = {'id': 10, 'size': 5, 'x': 2, 'y': 3}
        self.assertDictEqual(s.to_dictionary(), expected_dict)
