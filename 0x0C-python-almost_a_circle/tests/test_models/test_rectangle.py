#!/usr/bin/python3
"""Test files for rectangle.py"""
import unittest
import io
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test for instantiation of rectangle instance"""

    def test_instantiation(self):
        rect = Rectangle(10, 20)
        self.assertIsInstance(rect, Base)

    def test_private_attrs_1(self):
        rect = Rectangle(5, 8)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_private_attrs_2(self):
        rect2 = Rectangle(10, 20, 9)
        self.assertEqual(rect2.height, 20)
        self.assertEqual(rect2.width, 10)
        self.assertEqual(rect2.x, 9)
        self.assertEqual(rect2.y, 0)

    def test_private_attrs_3(self):
        rect3 = Rectangle(10, 20, 9, 56)
        self.assertEqual(rect3.height, 20)
        self.assertEqual(rect3.width, 10)
        self.assertEqual(rect3.x, 9)
        self.assertEqual(rect3.y, 56)

    def test_zero_argument(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_argument(self):
        with self.assertRaises(TypeError):
            Rectangle(10)


class TestAttributeType(unittest.TestCase):
    """Test for valid argument types"""

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            Rectangle("long", 5)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            Rectangle(5, "short")

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 6, 'origin')

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 6, 5, 'origin')


class TestAttributesValue(unittest.TestCase):
    """Test for valid argument values"""

    def test_incorrect_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_incorrect_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 0)

    def test_incorrect_x(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 6, -5, 0)

    def test_incorrect_y(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 6, 0, -6)


class TestRectangleArea(unittest.TestCase):
    """Test for the `area` method"""

    def test_small_area(self):
        """Test for small area"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_small_area_update(self):
        r2 = Rectangle(2, 10)
        r2.width = 3
        self.assertEqual(r2.area(), 30)
        r2.height = 100
        self.assertEqual(r2.area(), 300)

    def test_big_area(self):
        """Test for big areas"""
        rect = Rectangle(4654615454135437163418, 34131514365468403646540654)
        self.assertEqual(rect.area(),
                         158869074238554911050717840508459029666178595372)

    def test_area_with_invalid_argument(self):
        """Expecting `TypeError` when passing arguments"""
        rect = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            rect.area(42)


class TestRectangleDisplayAndPrint(unittest.TestCase):
    """Test for `display` and print method"""

    @staticmethod
    def get_stdout(obj, method) -> str:
        """returns the contents of `stdout` after performing method

        Args:
            obj (object): the object
            method (str): the method name to use

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

    def test_display(self):
        """Test for correct out put without `x` and `y`"""
        rect = Rectangle(4, 4)
        output = TestRectangleDisplayAndPrint.get_stdout(rect, 'display')
        self.assertMultiLineEqual(output, "####\n####\n####\n####\n")

    def test_print(self):
        rect = Rectangle(5, 5, 0, 0, 1)
        output = TestRectangleDisplayAndPrint.get_stdout(rect, 'print')
        correct = "[Rectangle] (1) 0/0 - 5/5\n"
        self.assertEqual(output, correct)

    def test_display_with_x(self):
        """Test for correct output with `x` and `y`"""
        rect = Rectangle(2, 2, 2, 0)
        output = TestRectangleDisplayAndPrint.get_stdout(rect, "display")
        self.assertMultiLineEqual(output, "  ##\n  ##\n")

    def test_display_with_y(self):
        rr = Rectangle(3, 3, 0, 5)
        output = TestRectangleDisplayAndPrint.get_stdout(rr, 'display')
        self.assertMultiLineEqual(output, "\n\n\n\n\n###\n###\n###\n")

    def test_display_with_xy(self):
        rect1 = Rectangle(2, 2, 2, 2)
        output = TestRectangleDisplayAndPrint.get_stdout(rect1, "display")
        self.assertMultiLineEqual(output, "\n\n  ##\n  ##\n")


class TestUpdate(unittest.TestCase):
    """Test for `update` method

    the methods defines are listed in the order the arguments
    should be passed - since argument order is super import
    when using `*args`"""

    def test_update_id(self):
        """Test for updating only `id` attribute"""
        rect = Rectangle(10, 10, 1, 2, 1)
        rect.update(100)
        self.assertEqual(rect.id, 100)

    def test_update_width(self):
        """Test for updating `id` and `width`"""
        rect = Rectangle(6, 5, 0, 0, 10)
        rect.update(100, 60)
        self.assertEqual(rect.id, 100)
        self.assertEqual(rect.width, 60)

    def test_update_height(self):
        """Test for updating `id`, `width` and `height`"""
        rect = Rectangle(6, 5, 0, 0, 10)
        rect.update(100, 60, 50)
        self.assertEqual(rect.id, 100)
        self.assertEqual(rect.width, 60)
        self.assertEqual(rect.height, 50)

    def test_update_x(self):
        """Test for updating `id`, `width`, `height` and `x`"""
        rect = Rectangle(6, 5, 1, 0, 10)
        rect.update(100, 60, 50, 10)
        self.assertEqual(rect.id, 100)
        self.assertEqual(rect.width, 60)
        self.assertEqual(rect.height, 50)
        self.assertEqual(rect.x, 10)

    def test_update_y(self):
        """Test for updating `id`, `width`, `height`, `x` and `y`"""
        rect = Rectangle(6, 5, 1, 1, 10)
        rect.update(100, 60, 50, 10, 10)
        self.assertEqual(rect.id, 100)
        self.assertEqual(rect.width, 60)
        self.assertEqual(rect.height, 50)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 10)

    def test_update_width_invalid(self):
        """Test for updating `id` and `width`"""
        rect = Rectangle(6, 5, 0, 0, 10)
        with self.assertRaises(TypeError):
            rect.update(100, {'short': 60})

    def test_update_height_invalid(self):
        """Test for updating `id`, `width` and `height`"""
        rect = Rectangle(6, 5, 0, 0, 10)
        with self.assertRaises(TypeError):
            rect.update(100, 60, True)

    def test_update_x_invalid(self):
        """Test for updating `id`, `width`, `height` and `x`"""
        rect = Rectangle(6, 5, 1, 0, 10)
        with self.assertRaises(ValueError):
            rect.update(100, 60, 50, -1)

    def test_update_y_invalid(self):
        """Test for updating `id`, `width`, `height`, `x` and `y`"""
        rect = Rectangle(6, 5, 1, 1, 10)
        with self.assertRaises(ValueError):
            rect.update(100, 60, 50, 10, -8)


class TestUpdateKWARGS(unittest.TestCase):
    """Test `update` method with key-worded arguments"""

    def test_args_and_kwargs(self):
        """`**kwargs` must be skipped is `*args` exists and is not empty"""
        rect = Rectangle(3, 8, 0, 0, 10)
        rect.update(100, 30, 80, 10, 10, id=10, width=42)
        self.assertEqual(rect.id, 100)
        self.assertEqual(rect.width, 30)

    def test_kwargs_only(self):
        """test for updating with `**kwargs`"""
        rect = Rectangle(10, 10)
        rect.update(width=50)
        self.assertEqual(rect.width, 50)

    def test_kwargs_random_order(self):
        """test updating in random attributes order"""
        rect = Rectangle(10, 10)
        rect.update(x=5, width=45, y=3, height=3)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.width, 45)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.height, 3)


class TestToDictionary(unittest.TestCase):
    """Tests for `to_dictionary` method"""

    def test_keys(self):
        """Test if the dictionary contains all keys/attributes"""
        rect = Rectangle(10, 5)
        my_dict = rect.to_dictionary()
        self.assertListEqual(sorted(my_dict.keys()), [
                             "height", "id", "width", "x", "y"])

    def test_values(self):
        """Test for correct dict value"""
        rect = Rectangle(10, 10, 1, 1, 12)
        my_dict = rect.to_dictionary()
        self.assertEqual(my_dict['height'], 10)
        self.assertEqual(my_dict['width'], 10)
        self.assertEqual(my_dict['x'], 1)
        self.assertEqual(my_dict['y'], 1)
        self.assertEqual(my_dict['id'], 12)
