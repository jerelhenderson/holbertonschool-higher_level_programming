#!/usr/bin/python3
"""
Test Module: Base
test_base.py - unittests for 'Base'
"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class test_square(unittest.TestCase):
    """ Class 'Square' tests """
    def test_square_fst(self):
        """ test first instance """
        s1 = Square(1)
        self.assertEqual(s1.size, 1)

    def test_square_upd(self):
        """ test instance update """
        s1 = Square(2)
        self.assertEqual(s1.size, 2)

    def test_square_neg(self):
        """ test negative instance """
        with self.assertRaises(ValueError) as err:
            s1 = Square(-1)
            self.assertEqual(str(err.exception), "width must be > 0"
