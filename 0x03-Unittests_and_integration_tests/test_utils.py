#!/usr/bin/env python3
"""
Test utils.py
"""
import unittest
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    calss TestAccessNestedMap
    """

    @parameterized.expand([
        [{"a": 1}, ("a"), 1],
        [{"a": {"b": 2}}, ("a"), {"b": 2}],
        [{"a": {"b": 2}}, ("a", "b"), 2]
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        test access nested map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        [{}, ("a")],
        [{"a": 1}, ("a", "b")]
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        test access nested map exception
        """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)
