#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, param
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """unittest to test GithubOrgClient class"""
    @parameterized.expand([
        param(org_name='google',
              resource="https://api.github.com/orgs/google"),
        param(org_name='abc',
              resource="https://api.github.com/orgs/abc")
    ])
    @patch('client.get_json')
    def test_org(self, mock_getJson, org_name, resource):
        """this method should test that GithubOrgClient.org returns the
        correct value"""
        GithubOrgClient(org_name).org
        mock_getJson.assert_called_once_with(resource)

    def test_public_repos_url(self):
        """this method test the public repos url
        should return a known payload
        """
        with patch.object(
                GithubOrgClient, 'org', new_callable=PropertyMock
        ) as org_mock:
            org_mock.return_value = {
                "repos_url":  'https://api.github.com/orgs/google/repos'
            }
            res = GithubOrgClient('google').org["repos_url"]
            self.assertEqual(res, 'https://api.github.com/orgs/google/repos')
