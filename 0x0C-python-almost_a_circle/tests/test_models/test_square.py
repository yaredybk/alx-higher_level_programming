#!/usr/bin/python3
"""unittest Square class"""
import unittest
from io import StringIO
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ test the Square that inherits from Rectangle class """

    def test_1square(self):
        """test initialization of suare class"""

        s1 = Square(5)
        t1 = "[Square] (1) 0/0 - 5"
        ta1 = 25
        td1 = """#####
#####
#####
#####
#####\n"""

        self.assertEqual(str(s1), t1)
        self.assertEqual(s1.area(), ta1)

        captured_output1 = StringIO()
        sys.stdout = captured_output1
        s1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output1.getvalue(), td1)

        t2 = "[Square] (2) 2/0 - 2"
        ta2 = 4
        td2 = """  ##
  ##\n"""

        s2 = Square(2, 2)
        self.assertEqual(str(s2), t2)
        self.assertEqual(s2.area(), ta2)

        captured_output2 = StringIO()
        sys.stdout = captured_output2
        s2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output2.getvalue(), td2)

        t3 = "[Square] (3) 1/3 - 3"
        ta3 = 9
        td3 = """


 ###
 ###
 ###\n"""
        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), t3)
        self.assertEqual(s3.area(), ta3)

        captured_output3 = StringIO()
        sys.stdout = captured_output3
        s3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output3.getvalue(), td3)

        print(f"end init test{s3}")

    def test_2square_size(self):
        """ test square size setter/getter methods"""

        s4 = Square(5)
        self.assertEqual(str(s4), "[Square] (4) 0/0 - 5")
        self.assertEqual(s4.size, 5)
        s4.size = 10
        self.assertEqual(str(s4), "[Square] (4) 0/0 - 10")

        with self.assertRaises(TypeError) as e1:
            s4.size = "9"
        self.assertEqual(str(e1.exception), "width must be an integer")

    def test_3square_setter_args(self):
        """ test square setter args and kwargs """

        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (5) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")
