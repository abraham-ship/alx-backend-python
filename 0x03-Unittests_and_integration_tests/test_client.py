#!/usr/bin/env python3
'''unittest for clientclass'''
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''tests for GithubOrgClient'''
    @parameterized.expand([
        ("google",),
        ("abc",),
        ])
    @patch('client.get_json', autospec=True)
    def test_org(self, org_name, mock_get_json):
        '''test that GithubOrgClient.org returns the correct value'''
        mock_response = {"org": "data", "example": "response"}
        mock_get_json.return_value = mock_response

        github_org_client = GithubOrgClient(org_name)

        result = github_org_client.org()

        mock_get_json.assert_called_once_with(GithubOrgClient.ORG_URL.
                                              format(org=org_name))

        self.assertEqual(result, mock_response)
