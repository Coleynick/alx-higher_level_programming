#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer_norm(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_lis_empty(self):
        self.assertIsNone(max_integer([]))

    def test_max_lis_singleElement(self):
        self.assertEqual(max_integer([8]), 8)

    def test_float(self):
        self.assertEqual(max_integer([1.5, 8.5, 3.5]), 3.5)
        self.assertEqual(max_integer([1.0, 7, 3]), 3)

    def test_mixed(self):
        self.assertEqual(max_integer([1, 2, 3.5, 4]), 4)
        self.assertEqual(max_integer([1, "2", 3, 4]), 4)
        self.assertEqual(max_integer(["a", "d", "c"]), "c")
