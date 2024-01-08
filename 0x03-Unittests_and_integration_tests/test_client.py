#!/usr/bin/python3
'''unittest for clientclass'''
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient, memoize


class TestGithubOrgClient(unittest.TestCase):
    '''tests for GithubOrgClient'''
    @parameterized.expand([
        ("google",),
        ("abc",),
        ])
    @patch('client.get_json', autospec=True)
    def test_org(self, org_name, mock_get_json):
        '''test that GithubOrgClient.org returns the correct value'''
        github_org_client = GithubOrgClient(org_name)
        result = github_org_client.org()

        mock_get_json.assert_called_once_with(GithubOrgClient.ORG_URL.
                                              format(org=org_name))
        self.assertEqual(result, {"org": "data", "example": "response"})
