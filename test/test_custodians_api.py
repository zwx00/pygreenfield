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
from pygreenfield.api.custodians_api import CustodiansApi  # noqa: E501
from pygreenfield.rest import ApiException


class TestCustodiansApi(unittest.TestCase):
    """CustodiansApi unit test stubs"""

    def setUp(self):
        self.api = CustodiansApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_stores_store_id_custodian_accounts_account_id_addresses_payment_method_get(self):
        """Test case for api_v1_stores_store_id_custodian_accounts_account_id_addresses_payment_method_get

        Get a deposit address for custodian  # noqa: E501
        """
        pass

    def test_api_v1_stores_store_id_custodian_accounts_account_id_delete(self):
        """Test case for api_v1_stores_store_id_custodian_accounts_account_id_delete

        Delete store custodian account  # noqa: E501
        """
        pass

    def test_api_v1_stores_store_id_custodian_accounts_account_id_get(self):
        """Test case for api_v1_stores_store_id_custodian_accounts_account_id_get

        Get store custodian account  # noqa: E501
        """
        pass

    def test_api_v1_stores_store_id_custodian_accounts_account_id_put(self):
        """Test case for api_v1_stores_store_id_custodian_accounts_account_id_put

        Update custodial account  # noqa: E501
        """
        pass

    def test_api_v1_stores_store_id_custodian_accounts_account_id_trades_market_post(self):
        """Test case for api_v1_stores_store_id_custodian_accounts_account_id_trades_market_post

        Trade one asset for another  # noqa: E501
        """
        pass

    def test_api_v1_stores_store_id_custodian_accounts_account_id_trades_quote_get(self):
        """Test case for api_v1_stores_store_id_custodian_accounts_account_id_trades_quote_get

        Get quote for trading one asset for another  # noqa: E501
        """
        pass

    def test_api_v1_stores_store_id_custodian_accounts_account_id_withdrawals_post(self):
        """Test case for api_v1_stores_store_id_custodian_accounts_account_id_withdrawals_post

        Withdraw to store wallet  # noqa: E501
        """
        pass

    def test_api_v1_stores_store_id_custodian_accounts_account_id_withdrawals_withdrawal_id_post(self):
        """Test case for api_v1_stores_store_id_custodian_accounts_account_id_withdrawals_withdrawal_id_post

        Get withdrawal info  # noqa: E501
        """
        pass

    def test_api_v1_stores_store_id_custodian_accounts_get(self):
        """Test case for api_v1_stores_store_id_custodian_accounts_get

        List store custodian accounts  # noqa: E501
        """
        pass

    def test_api_v1_stores_store_id_custodian_accounts_post(self):
        """Test case for api_v1_stores_store_id_custodian_accounts_post

        Add a custodial account to a store.  # noqa: E501
        """
        pass

    def test_custodians_get_supported_custodians(self):
        """Test case for custodians_get_supported_custodians

        List supported custodians  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
