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
from pygreenfield.api.store_payment_methods__lnurl_pay_api import StorePaymentMethodsLNURLPayApi  # noqa: E501
from pygreenfield.rest import ApiException


class TestStorePaymentMethodsLNURLPayApi(unittest.TestCase):
    """StorePaymentMethodsLNURLPayApi unit test stubs"""

    def setUp(self):
        self.api = StorePaymentMethodsLNURLPayApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_stores_store_id_payment_methods_lnurl_crypto_code_delete(self):
        """Test case for api_v1_stores_store_id_payment_methods_lnurl_crypto_code_delete

        Remove store LNURL Pay payment method  # noqa: E501
        """
        pass

    def test_store_lnurl_pay_payment_methods_get_lnurl_pay_payment_method(self):
        """Test case for store_lnurl_pay_payment_methods_get_lnurl_pay_payment_method

        Get store LNURL Pay payment method  # noqa: E501
        """
        pass

    def test_store_lnurl_pay_payment_methods_get_lnurl_pay_payment_methods(self):
        """Test case for store_lnurl_pay_payment_methods_get_lnurl_pay_payment_methods

        Get store LNURL payment methods  # noqa: E501
        """
        pass

    def test_store_lnurl_pay_payment_methods_update_lnurl_pay_payment_method(self):
        """Test case for store_lnurl_pay_payment_methods_update_lnurl_pay_payment_method

        Update store LNURL Pay payment method  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
