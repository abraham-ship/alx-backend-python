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

    def test_public_repos_url(self, mock_repos_url, mock_get_json):
        '''Mocking a property'''
        mock_payload = {"repos_url":
                        "https://api.github.com/orgs/example/repos"}

        with patch('client.GithubOrgClient.org', return_value=mock_payload):
            github_org_client = GithubOrgClient("dummy_org")

            result = github_org_client._public_repos_url

            self.assertEqual(result, mock_payload["repos_url"])

    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=unittest.mock.PropertyMock)
    @patch('client.get_json', autospec=True)
    def test_public_repos(self, mock_repos_url, mock_get_json):
        '''More patching'''
        mock_payload = {"repos_url": "https://api.github.com/\
                          orgs/example/repos"}
        mock_repos_url.return_value = mock_payload
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]

        github_org_client = GithubOrgClient("dummy_org")
        result = github_org_client.public_repos()

        self.assertEqual(result, ["repo1", "repo2"])
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/\
                                                orgs/example/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, license_key, expected_result):
        '''Parametize'''
        github_org_client = GithubOrgClient("dummy_org")
        result = github_org_client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)
