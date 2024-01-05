#!/usr/bin/env python3
'''unit test for utils.access_nested_map'''
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    '''unit tests for nested map function'''
    @parameterized.expand([
        [{"a": 1}, ("a",), 1],
        [{"a": {"b": 2}}, ("a",), {"b": 2}],
        [{"a": {"b": 2}}, ("a", "b"), 2]
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''test given input for expected result'''
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        [{}, ("a",), KeyError],
        [{"a": 1}, ("a", "b"), KeyError],
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        '''test for exception'''
        if expected == KeyError:
            with self.assertRaises(KeyError):
                access_nested_map(nested_map, path)
        else:
            result = access_nested_map(nested_map, path)
            self.assertEqual(result, expected)
