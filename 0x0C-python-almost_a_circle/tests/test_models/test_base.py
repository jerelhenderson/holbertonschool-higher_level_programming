#!/usr/bin/python3
"""
Test Module: Base
test_base.py - unittests for 'Base'
"""
import unittest
from models.base import Base


class test_base(unittest.TestCase):
    """ Class 'Base' tests """
    def test_id_fst(self):
        """ test first instance """
        b1 = Base(1)
        self.assertEqual(b1.id, 1)

    def test_id_upd(self):
        """ test instance update """
        b2 = Base(2)
        self.assertEqual(b2.id, 2)

    def test_id_neg(self):
        """ test negative instance """
        b3 = Base(-1)
        self.assertEqual(b3.id, -1)

    def test_id_emp(self):
        """ test empty instance """
        self.assertEqual(Base.from_json_string(None), [])

    def test_id_str(self):
        """ test string instance """
        b1 = Base("これからみんなでめちゃくちゃ踊ってさわごさわご")
        self.assertEqual(b1.id, "これからみんなでめちゃくちゃ踊ってさわごさわご")

    def test_id_lst(self):
        """ test list instance """
        b1 = Base([1, 2, 3])
        self.assertEqual(b1.id, [1, 2, 3])

    def test_id_int(self):
        """ test int instance """
        b1 = Base()
        self.assertEqual(type(b1.id), int)
