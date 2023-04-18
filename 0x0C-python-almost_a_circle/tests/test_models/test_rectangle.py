#!/usr/bin/python3
"""This test module defines tests for rectangle.py"""

from models.rectangle import Rectangle
from models.base import Base
import unittest


def setUp(self):
    Base._Base__nb_objects = 0

class TestRectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 10)
        with self.assertRaises(TypeError):
            r = Rectangle("five", 10)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, -1)
        with self.assertRaises(TypeError):
            r = Rectangle(5, "ten")

    def test_invalid_x(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, -1)
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, "zero")

    def test_invalid_y(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, 0, -1)
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, 0, "one")

    def test_area_calculation(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_create_rectangle_with_args(self):
        Base._Base__nb_objects = 0
        r = Rectangle(10, 5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_create_rectangle_with_kwargs(self):
        Base._Base__nb_objects = 0
        r = Rectangle(id=2, width=7, height=2, x=1, y=1)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_display(self):
        r = Rectangle(3, 2)
        output = "\n".join(["###", "###", ""])
        self.assertEqual(r.display(), print(output))

    def test_to_dictionary(self):
        Base._Base__nb_objects = 0
        r = Rectangle(10, 5, 2, 1)
        self.assertEqual(r.to_dictionary(), {
                         'id': 1, 'width': 10, 'height': 5, 'x': 2, 'y': 1})

    def test_update_kwargs(self):
        Base._Base__nb_objects = 0
        r = Rectangle(10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 10/1")

    def test_type(self):
        self.assertEqual(type(Rectangle), type)


if __name__ == "__main__":
    unittest.main()
