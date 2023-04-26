#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
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
