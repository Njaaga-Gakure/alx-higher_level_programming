#!/usr/bin/python3
"""Unittest for max_integer."""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max_integer module."""

    def test_unique_list(self):
        """Test with lists with unique values."""
        self.assertEqual(max_integer([4, 7, 9, 10]), 10)
        self.assertEqual(max_integer([10, 17, 9, 4]), 17)

    def test_repeated_list(self):
        """Test with lists with repeated values."""
        self.assertEqual(max_integer([4, 10, 9, 10]), 10)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([9, 7, 9, 3]), 9)

    def test_negative_list(self):
        """Test with lists with negative values."""
        self.assertEqual(max_integer([-4, -7, -2, -10]), -2)
        self.assertEqual(max_integer([-4, -7, 0, -10]), 0)
        self.assertEqual(max_integer([-5, -7, -3, -3]), -3)
        self.assertEqual(max_integer([-4, -5, 9, -17]), 9)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_float_list(self):
        """Test with a list with float values."""
        self.assertEqual(max_integer([2.2, 5.5, 1.6, 10.3]), 10.3)

    def test_null_list(self):
        """Test with a null list."""
        self.assertEqual(max_integer(), None)

    def test_non_int_list(self):
        """Test with a list with non-integer one or more values."""
        with self.assertRaises(TypeError):
            max_integer([1, [1, 2, 3], {"key": "value"}])
            max_integer([2, 'c', '5'])
