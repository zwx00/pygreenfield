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
from pygreenfield.api.lightning__internal_node_api import LightningInternalNodeApi  # noqa: E501
from pygreenfield.rest import ApiException


class TestLightningInternalNodeApi(unittest.TestCase):
    """LightningInternalNodeApi unit test stubs"""

    def setUp(self):
        self.api = LightningInternalNodeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_internal_lightning_node_api_connect_to_node(self):
        """Test case for internal_lightning_node_api_connect_to_node

        Connect to lightning node  # noqa: E501
        """
        pass

    def test_internal_lightning_node_api_create_invoice(self):
        """Test case for internal_lightning_node_api_create_invoice

        Create lightning invoice  # noqa: E501
        """
        pass

    def test_internal_lightning_node_api_get_balance(self):
        """Test case for internal_lightning_node_api_get_balance

        Get node balance  # noqa: E501
        """
        pass

    def test_internal_lightning_node_api_get_channels(self):
        """Test case for internal_lightning_node_api_get_channels

        Get channels  # noqa: E501
        """
        pass

    def test_internal_lightning_node_api_get_deposit_address(self):
        """Test case for internal_lightning_node_api_get_deposit_address

        Get deposit address  # noqa: E501
        """
        pass

    def test_internal_lightning_node_api_get_info(self):
        """Test case for internal_lightning_node_api_get_info

        Get node information  # noqa: E501
        """
        pass

    def test_internal_lightning_node_api_get_invoice(self):
        """Test case for internal_lightning_node_api_get_invoice

        Get invoice  # noqa: E501
        """
        pass

    def test_internal_lightning_node_api_get_payment(self):
        """Test case for internal_lightning_node_api_get_payment

        Get payment  # noqa: E501
        """
        pass

    def test_internal_lightning_node_api_open_channel(self):
        """Test case for internal_lightning_node_api_open_channel

        Open channel  # noqa: E501
        """
        pass

    def test_internal_lightning_node_api_pay_invoice(self):
        """Test case for internal_lightning_node_api_pay_invoice

        Pay Lightning Invoice  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
