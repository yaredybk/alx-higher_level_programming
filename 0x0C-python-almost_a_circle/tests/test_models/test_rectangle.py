#!/usr/bin/python3
""" unit tests for the Rectangle class"""
import unittest
from io import StringIO
from unittest.mock import patch
import sys
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """test Rectangl update"""


    def test_init(self):
        """test initialization"""
        r1 = Rectangle(10, 10, 10, 10)
        e1 = "[Rectangle] (1) 10/10 - 10/10"
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
        e1 = "[Rectangle] (1) 10/10 - 10/1"
        r2.update(height=1)
        self.assertEqual(str(r2), e1)

        e1 = "[Rectangle] (1) 2/10 - 1/1"
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
