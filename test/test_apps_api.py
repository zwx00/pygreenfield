# coding: utf-8

"""
    BTCPay Greenfield API

    A full API to use your BTCPay Server  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.apps_api import AppsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAppsApi(unittest.TestCase):
    """AppsApi unit test stubs"""

    def setUp(self):
        self.api = AppsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_apps_create_point_of_sale_app(self):
        """Test case for apps_create_point_of_sale_app

        Create a new Point of Sale app  # noqa: E501
        """
        pass

    def test_apps_delete_point_of_sale_app(self):
        """Test case for apps_delete_point_of_sale_app

        Delete app  # noqa: E501
        """
        pass

    def test_apps_get_point_of_sale_app(self):
        """Test case for apps_get_point_of_sale_app

        Get basic app data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
