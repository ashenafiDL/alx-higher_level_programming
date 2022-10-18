"""Unittests for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A class fofr testing the `max_integer([..])` function"""

    def test_int(self):
        """Tests for integers"""
        self.assertEqual(max_integer([98]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([85, 6, 3, 0, 2]), 85)
        self.assertEqual(max_integer([-9, 0, 5464, -64652]), 5464)

    def test_float(self):
        """Tests for floats"""
        self.assertEqual(max_integer([1.620]), 1.620)
        self.assertEqual(max_integer([5.3, -9.5, 6, 0, 10.62]), 10.61)

    def test_string(self):
        """Tests for strings"""
        self.assertEqual(max_integer("Holberton School"), 't')
        self.assertEqual(max_integer(
            ['Holberton', 'School', 'is', 'the', 'best', 'school']), 'the')

    def test_empty(self):
        """Tests for empty list and empty string"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(""), None)
