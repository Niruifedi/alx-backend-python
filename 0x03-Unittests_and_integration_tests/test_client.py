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

    @patch('client.get_json')
    def test_public_repos(self, mock_getJson):
        """this method unit-test GithubOrgClient.public_repos"""
        test = [
            {'id': 1, 'name': 'Docker'},
            {'id': 2, 'name': 'Kubernetes'},
            {'id': 2, 'name': 'Vagrant'}
        ]
        mock_getJson.return_value = test
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as public_repos_url_mock:
            public_repos_url_mock.return_value = 'https://github.com/org/abc'
            client0 = GithubOrgClient('abc')
            expected = ['Docker', 'Kubernetes', 'Vagrant']
            self.assertEqual(client0.public_repos(), expected)
            public_repos_url_mock.assert_called_once()
        mock_getJson.assert_called_once()
