# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import pygreenfield
from pygreenfield.api.users_api import UsersApi  # noqa: E501
from pygreenfield.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_users_get(self):
        """Test case for api_v1_users_get

        Get all users  # noqa: E501
        """
        pass

    def test_api_v1_users_id_or_email_delete(self):
        """Test case for api_v1_users_id_or_email_delete

        Delete user  # noqa: E501
        """
        pass

    def test_api_v1_users_id_or_email_get(self):
        """Test case for api_v1_users_id_or_email_get

        Get user by ID or Email  # noqa: E501
        """
        pass

    def test_api_v1_users_id_or_email_lock_delete(self):
        """Test case for api_v1_users_id_or_email_lock_delete

        Toggle user  # noqa: E501
        """
        pass

    def test_api_v1_users_post(self):
        """Test case for api_v1_users_post

        Create user  # noqa: E501
        """
        pass

    def test_users_delete_current_user(self):
        """Test case for users_delete_current_user

        Deletes user profile  # noqa: E501
        """
        pass

    def test_users_get_current_user(self):
        """Test case for users_get_current_user

        Get current user information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
