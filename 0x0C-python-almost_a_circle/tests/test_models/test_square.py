#!/usr/bin/python3
"""Test file for square.py"""
import unittest
import io
from contextlib import redirect_stdout
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Test for instantiation of square instance"""

    def test_instantiation(self):
        """Test if square instance inherits from `Rectangle` class"""
        sq = Square(10)
        self.assertIsInstance(sq, Rectangle)

    def test_private_attrs(self):
        """Test for correct value of private attributes"""
        sq = Square(5, 1, 2, 98)
        self.assertEqual(sq.width, 5)
        self.assertEqual(sq.x, 1)
        self.assertEqual(sq.y, 2)

    def test_num_of_args(self):
        """Test for exception raises when positional arguments omitted"""
        with self.assertRaises(TypeError):
            Square()


class TestPrintSquare(unittest.TestCase):
    """Test for printing square instance"""

    @staticmethod
    def get_stdout(obj, method) -> str:
        """gets the contents of standard output

        Args:
            obj (objects): the object
            method (str): the method to call

        Returns:
            str: the content of stdout
        """
        f = io.StringIO()
        with redirect_stdout(f):
            if method == 'print':
                print(obj)
            elif method == 'display':
                obj.display()
        return (f.getvalue())

    def test_print(self):
        sq = Square(2, 0, 0, 1)
        output = TestPrintSquare.get_stdout(sq, 'print')
        correct = "[Square] (1) 0/0 - 2\n"
        self.assertEqual(output, correct)

    def test_size_getter(self):
        """test for correct value of getter of `size`"""
        sq = Square(10)
        self.assertEqual(sq.size, 10)

    def test_size_setter(self):
        """test for setter of `size`"""
        sq = Square(7)
        sq.size = 100
        self.assertEqual(sq.size, 100)

    def test_size_setter_invalid(self):
        """test for setter of `size` with invalid argument"""
        sq = Square(7)

        with self.assertRaises(TypeError):
            sq.size = "very long side"


class TestUpdate(unittest.TestCase):
    """Test for `update` method

    the methods defines are listed in the order the arguments
    should be passed - since argument order is super import
    when using `*args`"""

    def test_update_id(self):
        """Test for updating only `id` attribute"""
        sq = Square(98)
        sq.update(2)
        self.assertEqual(sq.id, 2)

    def test_update_size(self):
        """Test for updating `id` and `size`"""
        sq = Square(98)
        sq.update(2, 100)
        self.assertEqual(sq.id, 2)
        self.assertEqual(sq.size, 100)

    def test_update_x(self):
        """Test for updating `id`, `size` and `x`"""
        sq = Square(98)
        sq.update(2, 100, 1)
        self.assertEqual(sq.id, 2)
        self.assertEqual(sq.size, 100)
        self.assertEqual(sq.x, 1)

    def test_update_y(self):
        """Test for updating `id`, `size`, `x` and `y`"""
        sq = Square(98)
        sq.update(2, 100, 1, 1)
        self.assertEqual(sq.id, 2)
        self.assertEqual(sq.size, 100)
        self.assertEqual(sq.x, 1)
        self.assertEqual(sq.y, 1)


class TestUpdateKWARGS(unittest.TestCase):
    """Test `update` method with key-worded arguments"""

    def test_args_and_kwargs(self):
        """`**kwargs` must be skipped is `*args` exists and is not empty"""
        sq = Square(3)
        sq.update(100, 30, 1, 1, id=10, size=42)
        self.assertEqual(sq.id, 100)
        self.assertEqual(sq.size, 30)

    def test_kwargs_only(self):
        """test for updating with `**kwargs`"""
        sq = Square(10)
        sq.update(size=50)
        self.assertEqual(sq.size, 50)

    def test_kwargs_random_order(self):
        """test updating in random attributes order"""
        sq = Square(10, 10)
        sq.update(x=5, size=45, y=3)
        self.assertEqual(sq.x, 5)
        self.assertEqual(sq.size, 45)
        self.assertEqual(sq.y, 3)


class TestToDictionary(unittest.TestCase):
    """Tests for `to_dictionary` method"""

    def test_keys(self):
        """Test if the dictionary contains all keys/attributes"""
        sq = Square(5)
        my_dict = sq.to_dictionary()
        self.assertListEqual(sorted(my_dict.keys()), ["id", "size", "x", "y"])

    def test_values(self):
        """Test for correct dict value"""
        sq = Square(10, 1, 1, 12)
        my_dict = sq.to_dictionary()
        self.assertEqual(my_dict['size'], 10)
        self.assertEqual(my_dict['x'], 1)
        self.assertEqual(my_dict['y'], 1)
        self.assertEqual(my_dict['id'], 12)
