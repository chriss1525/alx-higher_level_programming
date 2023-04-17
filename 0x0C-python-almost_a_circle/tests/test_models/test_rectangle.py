#!/usr/bin/python3
"""This test module defines tests for rectangle.py"""

from models.rectangle import Rectangle
import unittest


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


    def test_attribute(self):  
        b = Rectangle()
        with self.assertRaises(AttributeError):
            print(b.nb_objects)

    def test_type(self):
        self.assertEqual(type(Rectangle), type)