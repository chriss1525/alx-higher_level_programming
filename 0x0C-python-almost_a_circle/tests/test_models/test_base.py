#!/usr/bin/python3
"""This test module defines tests for base.py"""

from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        Base._Base__nb_objects = 0
        # Test that the id attribute is set correctly when provided
        obj = Base(42)
        self.assertEqual(obj.id, 42)

    def test_init_without_id(self):
        Base._Base__nb_objects = 0
        # Test that the id attribute is incremented correctly when not provided
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_type(self):
        self.assertEqual(type(Base), type)

    def test_to_json_string(self):
        Base._Base__nb_objects = 0
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(
            [{'id': 1, 'x': 2, 'y': 3}]), '[{"id": 1, "x": 2, "y": 3}]')

    def test_save_to_file(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(
            ), '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]')

    def test_create(self):
        Base._Base__nb_objects = 0
        r1_dict = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        r1 = Rectangle.create(**r1_dict)
        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 2/8 - 10/7")

    def test_load_from_file(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        lst = Rectangle.load_from_file()
        self.assertIsInstance(lst, list)
        self.assertEqual(len(lst), 2)
        self.assertIsInstance(lst[0], Rectangle)
        self.assertEqual(lst[0].__str__(), "[Rectangle] (1) 2/8 - 10/7")
        self.assertIsInstance(lst[1], Rectangle)
        self.assertEqual(lst[1].__str__(), "[Rectangle] (2) 0/0 - 2/4")


if __name__ == "__main__":
    unittest.main()
