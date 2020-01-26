#!/usr/bin/python3
"""
Test Module: Base
test_base.py - unittests for 'Base'
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):
    """ Class 'Rectangle' tests """
    def test_rectangle_fst(self):
        """ test first instance """
        r1 = Rectangle(1, 1)
        self.assertEqual(Rectangle, 1, 1)

    def test_rectangle_upd(self):
        """ test instance update """
        r1 = Rectangle(2, 2)
        self.assertEqual(Rectangle, 2, 2)

    def test_rectangle_neg(self):
        """ test negative instance """
        with self.assertRaises(ValueError) as err:
            s1 = Rectangle(-1, -1)
            self.assertEqual(str(err.exception), "width must be > 0")
