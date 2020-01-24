#!/usr/bin/python3
"""
Test Module: Base
test_base.py - unittests for 'Base'
"""
import unittest
from models.base import Base


class test_base(unittest.TestCase):
    """ Class 'Base' tests """
    def test_id_value1(self):
        """testing if id updates properly"""
        instance1 = Base()
        self.assertEqual(instance1.id, 1)

    def test_id_value2(self):
        """testing if id updates when given specific val"""
        instance2 = Base(10)
        self.assertEqual(instance2.id, 10)

    def test_id_value3(self):
        """testing if id updates correctly with neg val"""
        instance3 = Base(-10)
        self.assertEqual(instance3.id, -10)

    def test_id_value4(self):
        """testing if id updates with list val"""
        instance4 = Base([1, 2, 3])
        self.assertEqual(instance4.id, [1, 2, 3])

    def test_id_value5(self):
        """testing if id updates with string val"""
        instance5 = Base("hi")
        self.assertEqual(instance5.id, "hi")

    def test_id_value6(self):
        """testing if id updates with no given val"""
        instance6 = Base()
        self.assertEqual(instance6.id, 2)
