#!/usr/bin/python3
""" unit tests for the Rectangle class"""
import unittest
from io import StringIO
from unittest.mock import patch
import sys
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle_init(unittest.TestCase):
    """Unittest for initialization of rectangle"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10,2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_id_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_id_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_id_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_id_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2, 3, 4, 5).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)


class TestRectangle_update(unittest.TestCase):
    """test Rectangle update"""


    def test_init(self):
        """test initialization"""
        r1 = Rectangle(10, 10, 10, 10)
        e1 = f"[Rectangle] ({r1.id}) 10/10 - 10/10"
        self.assertEqual(str(r1), e1)

    def test_upadet_via_args(self):
        """test for class update method using args"""
        e1 = "[Rectangle] (89) 10/10 - 10/10"
        r2 = Rectangle(10, 10, 10, 10)
        r2.update(89)
        self.assertEqual(str(r2), e1)
        e1 = "[Rectangle] (89) 10/10 - 2/10"
        r2.update(89, 2)
        self.assertEqual(str(r2), e1)
        e1 = "[Rectangle] (89) 10/10 - 2/3"
        r2.update(89, 2, 3)
        self.assertEqual(str(r2), e1)
        e1 = "[Rectangle] (89) 4/10 - 2/3"
        r2.update(89, 2, 3, 4)
        self.assertEqual(str(r2), e1)
        e1 = "[Rectangle] (89) 4/5 - 2/3"
        r2.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r2), e1)

class TestRectangle2(unittest.TestCase):
    """ test rectangle 2 """

    def test_upadet_via_args(self):
        """test for class update method using kwargs"""

        r2 = Rectangle(10, 10, 10, 10)
        e1 = f"[Rectangle] ({r2.id}) 10/10 - 10/1"
        r2.update(height=1)
        self.assertEqual(str(r2), e1)

        e1 = f"[Rectangle] ({r2.id}) 2/10 - 1/1"
        r2.update(width=1, x=2)
        self.assertEqual(str(r2), e1)

        e1 = "[Rectangle] (89) 3/1 - 2/1"
        r2.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r2), e1)

        e1 = "[Rectangle] (89) 1/3 - 4/2"
        r2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r2), e1)

    def test_str_method(self):
        """test str method"""
        ex1 = "[Rectangle] (12) 2/1 - 4/6"
        re1 = str(Rectangle(4, 6, 2, 1, 12))
        self.assertEqual(ex1, re1)

    def test_display_method(self):
        """test str method"""

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            Rectangle(2, 3, 2, 2).display()
        ex1 ="""\n\n  ##\n  ##\n  ##\n"""
        re1 = Rectangle(2, 3, 2, 2)
        self.assertEqual(mock_stdout.getvalue(), ex1)
