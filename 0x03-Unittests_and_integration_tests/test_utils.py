#!/usr/bin/env python3
'''unit test for utils.access_nested_map'''
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
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


class TestGetJson(unittest.TestCase):
    '''tests for get_json function'''
    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        '''test for expected result from given inputs'''
        test_url_1 = "http://example.com"
        test_payload_1 = {"payload": True}
        mock_response_1 = Mock()
        mock_response_1.json.return_value = test_payload_1
        mock_get.return_value = mock_response_1

        result_1 = get_json(test_url_1)
        mock_get.assert_called_once_with(test_url_1)
        self.assertEqual(result_1, test_payload_1)

        test_url_2 = "http://holberton.io"
        test_payload_2 = {"payload": False}
        mock_response_2 = Mock()
        mock_response_2.json.return_value = test_payload_2
        mock_get.return_value = mock_response_2

        result_2 = get_json(test_url_2)
        mock_get.assert_called_with(test_url_2)
        self.assertEqual(result_2, test_payload_2)


class TestMemoize(unittest.TestCase):
    '''tests for memoize function'''
    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        test_object = self.TestClass()

        result_1 = test_object.a_property
        result_2 = test_object.a_property
        mock_a_method.assert_called_once()
