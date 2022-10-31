#!/usr/bin/python3
"""Tests files for base.py"""
import os
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unit test for instantiation of a `Base` class."""

    def test_empty_id(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)

    def test_none_id(self):
        base2 = Base(None)
        base3 = Base(None)
        self.assertAlmostEqual(base3.id, base2.id + 1)

    def test_int_id(self):
        base12 = Base(12)
        self.assertEqual(base12.id, 12)

    def test_float_id(self):
        base_float = Base(98.2)
        self.assertEqual(base_float.id, 98.2)

    def test_multiple_id(self):
        b1 = Base()
        b5 = Base(5)
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)


class TestToJsonString(unittest.TestCase):
    """Tests for `to_json_string` method"""

    def test_type(self):
        output = Base.to_json_string(list_dictionaries=None)
        self.assertIsInstance(output, str)

    def test_empty(self):
        """Test for empty dictionary"""
        output = Base.to_json_string(list_dictionaries=None)
        self.assertEqual("[]", output)

    def test_correct_output(self):
        """Test for correct output"""
        rect = Rectangle(10, 5, 0, 0, 1)
        my_dict = rect.to_dictionary()
        output = Base.to_json_string(my_dict)
        self.assertIsInstance(output, str)
        self.assertEqual(output,
                         '{"id": 1, "width": 10, "height": 5, "x": 0, "y": 0}')


class TestSaveToFile(unittest.TestCase):
    """Tests for the method `save_to_file`"""

    def test_content_rectangle(self):
        rect = Rectangle(2, 3, 0, 0, 1)
        Base.save_to_file([rect])
        with open('Rectangle.json', mode='r') as file:
            self.assertEqual(
                file.read(),
                '{"id": 1, "width": 2, "height": 3, "x": 0, "y": 0}')

    def tearDown(self) -> None:
        try:
            os.remove('Rectangle.json')
            os.remove('Square.json')
        except Exception as _:
            pass
