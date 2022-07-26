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
from swagger_client.api.stores__payouts_api import StoresPayoutsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStoresPayoutsApi(unittest.TestCase):
    """StoresPayoutsApi unit test stubs"""

    def setUp(self):
        self.api = StoresPayoutsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_payouts_create_payout_through_store(self):
        """Test case for payouts_create_payout_through_store

        Create Payout   # noqa: E501
        """
        pass

    def test_pull_payments_approve_payout(self):
        """Test case for pull_payments_approve_payout

        Approve Payout  # noqa: E501
        """
        pass

    def test_pull_payments_cancel_payout(self):
        """Test case for pull_payments_cancel_payout

        Cancel Payout  # noqa: E501
        """
        pass

    def test_pull_payments_get_store_payouts(self):
        """Test case for pull_payments_get_store_payouts

        Get Store Payouts  # noqa: E501
        """
        pass

    def test_pull_payments_mark_payout_paid(self):
        """Test case for pull_payments_mark_payout_paid

        Mark Payout as Paid  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()