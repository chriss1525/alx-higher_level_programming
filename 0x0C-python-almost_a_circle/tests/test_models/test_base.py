#!/usr/bin/python3
"""This test module defines tests for base.py"""

from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        # Test that the id attribute is set correctly when provided
        obj = Base(42)
        self.assertEqual(obj.id, 42)

    def test_init_without_id(self):
        # Test that the id attribute is incremented correctly when not provided
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_type(self):
        self.assertEqual(type(Base), type)


if __name__ == "__main__":
    unittest.main()
