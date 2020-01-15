#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_pos_integers(self):
        self.assertEqual(max_integer([10, 20, 30, 40, 50]), 50)

    def test_neg_integers(self):
        self.assertEqual(max_integer([-50, -40, -30, -20, -10]), -10)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4, 5.5]), 5.5)

    def test_strings(self):
        self.assertEqual(max_integer("Holberton"), 't')

    def test_no_input(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_integer((1, "bob"))

    def test_mixed_ints(self):
        self.assertEqual(max_integer([-50.5, -50, 0, 50, 50.5]), 50.5)


if __name__ == '__main__':
    unittest.main()
