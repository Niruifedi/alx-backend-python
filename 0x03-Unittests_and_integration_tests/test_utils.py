#!/usr/bin/env python3
"""
Test utils.py
"""
import unittest
import requests
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """
    class TestGetJson
    """
    @parameterized.expand([
            ["http://example.com", {"payload": True}],
            ["http://holberton.io", {"payload": False}]
        ])
    def test_get_json(self, test_url, test_payload):
        """
            test get json
        """
        with patch('requests.get') as mock_get:
            mock_get.return_value.ok = test_payload.get("payload")
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test class for Momoization
    """
    def test_memoize(self):
        """
        Test Memoize
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock.assert_called_once()
